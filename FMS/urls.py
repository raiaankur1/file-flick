from django.urls import re_path, path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  re_path('FMS/login', views.login),
  re_path('FMS/signup', views.signup),
  re_path('FMS/loaduser', views.get_user),
  re_path('FMS/userupload', views.user_upload),
  re_path('FMS/guestupload', views.guest_upload),
  re_path('FMS/recent', views.recent),
  re_path('FMS/delete', views.delete_upload),
  path('download/<str:shortuid>', views.download),
]