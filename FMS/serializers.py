from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Upload, URL

class UserSerializer(serializers.ModelSerializer):
  class Meta(object):
    model = User
    fields = ['username', 'password', 'email']


class UploadSerializer(serializers.Serializer):
  url = serializers.CharField(required = False)
  owner = serializers.CharField(allow_null = True)
  file = serializers.FileField(max_length = 100000 , allow_empty_file = False , use_url = False)
  filename = serializers.CharField(required = False)
  

  def create(self , validated_data):
      url = URL.objects.create()
      owner = validated_data.pop('owner')
      file = validated_data.pop('file')
      if owner is not None:
        user = User.objects.get(username=owner)
        upload = Upload.objects.create(url = url, owner = user, file = file, filename = file.name)
      else:
        upload = Upload.objects.create(url = url , file = file, filename = file.name)

      return {'file' : {}, 'url' : str(url.uid), 'owner': str(upload.owner), 'filename': str(upload.filename)}
