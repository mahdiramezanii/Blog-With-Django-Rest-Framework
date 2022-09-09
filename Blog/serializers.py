from rest_framework import serializers
from Blog.models import Article,Comment


class CommentSerializer(serializers.ModelSerializer):
    article=serializers.SlugRelatedField(slug_field="discription",read_only=True)

    class Meta:
        model=Comment
        fields="__all__"

class ArticleSerializer(serializers.ModelSerializer):
    comment=serializers.SlugRelatedField(slug_field="text",read_only=True,many=True)
    image=serializers.SerializerMethodField()
    class Meta:
        model=Article
        fields="__all__"
        read_only_fields=["id","comment"]

    def get_image(self,obj):

        request=self.context.get("request")

        if obj.image != None:
            image_url=obj.image.url

            return request.build_absolute_uri(image_url)

        return None






