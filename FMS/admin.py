from django.contrib import admin

from .models import URL, Upload

admin.site.register(URL)
admin.site.register(Upload)