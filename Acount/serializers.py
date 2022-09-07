from rest_framework import serializers
from django.contrib.auth.models import User


class Userserializer(serializers.ModelSerializer):
    username=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = "__all__"

