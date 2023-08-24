from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Upload(models.Model):
  uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
  owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_DEFAULT, related_name="uploads")
  file = models.FileField(upload_to="uploads/")
  filename = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)


