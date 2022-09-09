from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from Blog.models import Article
from Blog.serializers import ArticleSerializer,CommentSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permisions import CostomPermision
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class ArticleView(APIView):


    def get(self,request):
        instance=Article.objects.all()
        paginator=PageNumberPagination()

        queryset=paginator.paginate_queryset(instance,request=request)

        serializer=ArticleSerializer(instance=queryset,many=True,context={"request":request})


        return Response(data=serializer.data)


class ArticleDetail(APIView):

    def post(self,request,pk):
        query_set=Article.objects.get(id=pk)
        serializer=ArticleSerializer(instance=query_set,context={"request":request})


        return Response(data=serializer.data)


class ArticleAddView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self,request):

        serializer=ArticleSerializer(data=request.data)



        if serializer.is_valid():

            if request.user.is_authenticated:
                serializer.validated_data["user"]=request.user

            serializer.save()

            return Response({"message":"added"},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CostomPermision]

    def put(self,request,pk):

        instance=Article.objects.get(id=pk)

        self.check_object_permissions(request,instance)

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


class CommentArticle(APIView):

    def get(self,request,pk):

        instance=Article.objects.get(id=pk).comment.all()

        serializer=CommentSerializer(instance=instance,many=True)


        return Response(serializer.data,status=status.HTTP_200_OK)










