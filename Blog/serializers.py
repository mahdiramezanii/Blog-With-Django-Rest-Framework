from rest_framework import serializers
from Blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Article
        fields="__all__"