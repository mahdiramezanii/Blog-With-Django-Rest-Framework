from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from Acount.serializers import Userserializer
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):

    def post(self,request):

        serializer=Userserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message":"User added"},status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


