from lib2to3.pgen2 import token
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from weldingDragonApp import serializers
from weldingDragonApp.serializers import UserSerializer

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        tokenData = {"username": request.data["username"],
                    "password": request.data["password"]}
        
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        