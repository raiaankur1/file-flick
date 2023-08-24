from django.urls import re_path
from . import views

urlpatterns = [
  re_path('login', views.login),
  re_path('signup', views.signup),
  re_path('userupload', views.user_upload),
  re_path('guestupload', views.guest_upload),
  re_path('recent', views.recent),
  re_path('delete', views.delete_upload),
  re_path('download/<str:shortuid>', views.download),
]