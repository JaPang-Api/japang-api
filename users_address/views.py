from .serializers import AddressSerializer
from users_address.models import Address
from rest_framework import viewsets

from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


# Create your views here.

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset =  Address.objects.all()
    serializer_class = AddressSerializer

class AddressView(APIView):
    def get(self, request):
        token = request.COOKIES.get('authorizationToken')

        if not token:
            # raise AuthenticationFailed('Unauthenticated!')
            return Response({
                'code' : 400,
                'message': 'authorizationToken not found!'
            }, status=400)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # raise AuthenticationFailed('Unauthenticated!')
            return Response({
                'code' : 400,
                'message': 'authorizationToken expires!'
            }, status=400)

        address = Address.objects.filter(users_id=payload['id']).first()
        serializer = AddressSerializer(address)
        return Response(serializer.data)
        # return Response({
        #     'error': None,
        #     'data': serializer.data
        # }, status=200)
