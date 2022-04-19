from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.http import HttpResponse
from xendit import Xendit

from payments.models import Payments as p
from .serializers import PaymentsSerializer

import json
import jwt, datetime

from rest_framework import viewsets


# Payments with share whatsapp and email.
class Payments(APIView):
    def post(self, request):

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

        api_key = "xnd_development_remFZWhJHVXRTHGxRVAS07T75IDJBZExEWJmEWuSArWyy5DNnQwfQ8NtqLX0Do"

        xendit_instance = Xendit(api_key=api_key)
        Invoice = xendit_instance.Invoice

        data = json.loads(request.body.decode("utf-8"))
        external_id = data.get('external_id')
        amount = data.get('amount')
        payer_email = data.get('payer_email')
        description = data.get('description')
        mobile_number = data.get('mobile_number')

        current_date_and_time = datetime.datetime.now()
        hours = 1
        hours_added = datetime.timedelta(hours = hours)

        expiry_date = current_date_and_time + hours_added

        customer = {
            "mobile_number": "+"+str(mobile_number)
        }

        customerNotificationPreference = {
            "invoice_created": [
                "email",
                "whatsapp",
                "sms"
            ],
            "invoice_reminder": [
                "email",
                "whatsapp",
                "sms"
            ],
            "invoice_expired": [
                "email",
                "whatsapp",
                "sms"
            ],
            "invoice_paid": [
                "email",
                "whatsapp",
                "sms"
            ]
        }

        invoice = Invoice.create(
            external_id=external_id,
            amount=amount,
            payer_email=payer_email,
            description=description,
            customer=customer,
            expiry_date=str(expiry_date),
            customer_notification_preference = customerNotificationPreference,
        )

        paya = p.objects.create(
            users_id=payload['id'],
            invoice_id=invoice.id,
            invoice_url=invoice.invoice_url,
            expiry_date=invoice.expiry_date,
            status=invoice.status,
            amount=invoice.amount
        )
        paya.save()

        return HttpResponse(invoice, content_type="application/json")

# Payments with share email.
class Invoice(APIView):
    def post(self, request):

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

        api_key = "xnd_development_remFZWhJHVXRTHGxRVAS07T75IDJBZExEWJmEWuSArWyy5DNnQwfQ8NtqLX0Do"

        xendit_instance = Xendit(api_key=api_key)
        Invoice = xendit_instance.Invoice

        data = json.loads(request.body.decode("utf-8"))
        external_id = data.get('external_id')
        amount = data.get('amount')
        payer_email = data.get('payer_email')
        description = data.get('description')
        should_send_email = data.get('should_send_email')

        invoice = Invoice.create(
            external_id=external_id,
            amount=amount,
            payer_email=payer_email,
            description=description,
            should_send_email=should_send_email,
        )

        paya = p.objects.create(
            users_id=payload['id'],
            invoice_id=invoice.id,
            invoice_url=invoice.invoice_url,
            expiry_date=invoice.expiry_date,
            status=invoice.status,
            amount=invoice.amount
        )
        paya.save()

        return HttpResponse(invoice, content_type="application/json")

class GetInvoice(APIView):
    def get(self, request):

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

        api_key = "xnd_development_remFZWhJHVXRTHGxRVAS07T75IDJBZExEWJmEWuSArWyy5DNnQwfQ8NtqLX0Do"

        xendit_instance = Xendit(api_key=api_key)
        Invoice = xendit_instance.Invoice

        invoice = Invoice.get(
            invoice_id="62355d5af26b5d28d9c7748a",
        )

        return HttpResponse(invoice, content_type="application/json")