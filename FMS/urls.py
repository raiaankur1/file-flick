from django.urls import re_path, path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  re_path('login', views.login),
  re_path('signup', views.signup),
  re_path('loaduser', views.get_user),
  re_path('userupload', views.user_upload),
  re_path('guestupload', views.guest_upload),
  re_path('recent', views.recent),
  re_path('delete', views.delete_upload),
  path('download/<str:shortuid>', views.download),
]