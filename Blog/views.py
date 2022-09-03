from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(["POST","GET"])
def tset(requset):


    return Response({"messgae":"Hi"})



