from rest_framework import serializers
from Blog.models import Article,Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Article
        fields="__all__"
        read_only_fields=["id",]

class CommentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=Comment
        fields="__all__"