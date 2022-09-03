from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from Blog.models import Article
from Blog.serializers import ArticleSerializer
from rest_framework import status
# @api_view(["POST","GET"])
# def tset(requset):
#
#
#     return Response({"messgae":"Hi"})


class ArticleView(APIView):

    def get(self,request):
        instance=Article.objects.all()

        serializer=ArticleSerializer(instance=instance,many=True)


        return Response(data=serializer.data)


class ArticleDetail(APIView):

    def post(self,request,pk):
        query_set=Article.objects.get(id=pk)
        serializer=ArticleSerializer(instance=query_set)


        return Response(data=serializer.data)


class ArticleAddView(APIView):

    def post(self,request):

        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message":"added"},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleUpdateView(APIView):

    def put(self,request,pk):
        instance=Article.objects.get(id=pk)
        serializer=ArticleSerializer(data=request.data,partial=True)

        if serializer.is_valid():
            serializer.update(instance=instance,validated_data=serializer.validated_data)
            serializer.save()

            return Response({"message":"Updated"},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDeleteView(APIView):

    def delete(self,request,pk):
        instance=Article.objects.get(id=pk)
        instance.delete()

        return Response({"message":"deleted"},status=status.HTTP_200_OK)









