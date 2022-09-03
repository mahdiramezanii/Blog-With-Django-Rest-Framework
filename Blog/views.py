from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from Blog.models import Article
from Blog.serializers import ArticleSerializer

@api_view(["POST","GET"])
def tset(requset):


    return Response({"messgae":"Hi"})


class ArticleView(APIView):

    def get(self,request):
        instance=Article.objects.all()

        serializer=ArticleSerializer(instance=instance,many=True)


        return Response(data=serializer.data)




