from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Upload

class UserSerializer(serializers.ModelSerializer):
  class Meta(object):
    model = User
    fields = ['username', 'password', 'email']


class UploadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Upload
    fields = ('id', 'owner', 'file', 'filename', 'created_at')
  # file = serializers.FileField(max_length= )
