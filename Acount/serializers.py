from rest_framework import serializers
from django.contrib.auth.models import User
from Blog.models import Article
from Blog.serializers import ArticleSerializer

class Userserializer(serializers.ModelSerializer):
    article=serializers.SerializerMethodField()
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields=["username"]


    def get_article(self,obj):

        instance=ArticleSerializer(instance=obj.article.all(),many=True)
        return instance.data
