from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from  . import serializers
from rest_framework.authtoken.models import Token
from . import signals


# only creating user or login process
# class RegistrationView(APIView):
#     def post(self, request):
#         serializers = RegistrationSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#         return Response(serializers.data, status= status.HTTP_400_BAD_REQUEST)



#complete registration process
class RegistrationView(APIView):
    def post(self, request):
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else:
            data = serializer.errors
        return Response(data)
   
    
# logout process:
class LogoutView(APIView):
        def post(self, request):
            request.user.auth_token.delete()
            return Response(status = status.HTTP_200_OK)