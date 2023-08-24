from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import shortuuid
import os


from django.db import models


class ShortUUIDField(models.UUIDField):
    def create_uuid(self):
        return shortuuid.uuid()

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', self.create_uuid)
        kwargs.setdefault('editable', False)
        kwargs.setdefault('unique', True)
        kwargs.setdefault('max_length', 10)
        super().__init__(*args, **kwargs)



class URL(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    short_uid = ShortUUIDField()
    original_url = models.URLField(blank=True, null=True)


def get_upload_path(instance, filename):
  filename = '{}.{}'.format(str(instance.url.uid),filename.split('.')[-1])
  return os.path.join("uploads/", filename)


class Upload(models.Model):
    url = models.OneToOneField(
        URL, blank=True, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, default=None, blank=True, null=True,
                              on_delete=models.SET_DEFAULT, related_name="uploads")
    file = models.FileField(upload_to=get_upload_path)
    filename = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
