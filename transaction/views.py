from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.http import HttpResponse
from xendit import Xendit

from transaction.models import Transaction as p
from order.models import Order

from cart.models import CartItem
from cart.serializers import CartItemSerializer

from users.models import User
from users.serializers import UsersSerializer

import json
import jwt, datetime

from rest_framework import viewsets

# Create your views here.

class Transaction(APIView):

    def post(self, request):

        # Cek Token User
        token = request.COOKIES.get('authorizationToken')

        if not token:
            # raise AuthenticationFailed('Unauthenticated!')
            return Response({
                'error':{
                    'code' : 400,
                    'message': 'authorizationToken not found!'
                },
                'data': None
            }, status=400)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # raise AuthenticationFailed('Unauthenticated!')
            return Response({
                'error':{
                    'code' : 400,
                    'message': 'authorizationToken expires!'
                },
                'data': None
            }, status=400)
        # End Cek Token User

        # Api Xendit (Invoice)
        api_key = "xnd_development_remFZWhJHVXRTHGxRVAS07T75IDJBZExEWJmEWuSArWyy5DNnQwfQ8NtqLX0Do"
        xendit_instance = Xendit(api_key=api_key)
        Invoice = xendit_instance.Invoice
        # End Api Xendit

        # Get Data From User
        user =  User.objects.filter(id=payload['id']).first()
        users = UsersSerializer(user)

        dump_user = json.dumps(users.data)
        dump_users = json.loads(dump_user)
        # End Get Data From User

        data = json.loads(request.body.decode("utf-8"))
        
        # Data From User
        payer_email = dump_users["email"]
        # mobile_number = dump_users["phone"]

        # Request
        external_id = data.get('external_id')
        description = data.get('description')
        should_send_email = data.get('should_send_email')
        amount = data.get('amount')
        delivery_address = data.get('delivery_address')

        # customer = {
        #     "mobile_number": "+"+str(mobile_number)
        # }

        # Invoice Xendit
        invoice = Invoice.create(
            external_id=external_id,
            amount=amount,
            payer_email=payer_email,
            description=description,
            should_send_email=should_send_email,
            # customer=customer,
        )

        # Transaction
        paya = p.objects.create(
            invoice_no=invoice.external_id,
            invoice_id=invoice.id,
            user_id=payload['id'],
            invoice_url=invoice.invoice_url,
            amount=invoice.amount,
            status=invoice.status,
            expiry_date=invoice.expiry_date,
            delivery_address=delivery_address
        )
        paya.save()

        # Transaction Detail 
        cart =  CartItem.objects.filter(user_id=payload['id'])
        carts = CartItemSerializer(cart, many=True)

        dump_cart = json.dumps(carts.data)
        dump_carts = json.loads(dump_cart)

        for list in dump_carts:

            order = Order.objects.create(
                amount = list["amount"],
                product_id = list["product"],
                user_id = list["user"],
                transaction_id = invoice.external_id
            )

            order.save()
        
        # Delete Cart By User Transaksi
        CartItem.objects.filter(user_id=payload['id']).delete()

        return HttpResponse(
            invoice, 
            content_type="application/json"
        )

class Callback(APIView):

    def post(self, request):

        # Api Xendit (Invoice)
        # apa = request.data
        data = json.loads(request.body.decode("utf-8"))

        id = data.get('id')
        statuss = data.get('status')

        p.objects.filter(invoice_id=id).update(status=statuss)

        return Response({
            'error': None,
            'message': 'Callback Xendit',
            'data': {
                'id': id,
                'status': statuss
            }
        }, status=200)