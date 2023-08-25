from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .serializers import UserSerializer, UploadSerializer
from .utilities import generate_s3_download_url, delete_s3_object, get_s3_file
from .models import Upload, URL

@api_view(['POST'])
def login(request):
  # print(request.data)
  user = get_object_or_404(User, username=request.data['username'])
  if not user.check_password(request.data['password']):
    return Response({"msg": "Not found."}, status=status.HTTP_404_NOT_FOUND)
  token, created = Token.objects.get_or_create(user=user)
  serializer = UserSerializer(instance=user)
  response = Response({"token": token.key, "user": serializer.data})
  response['Access-Control-Allow-Origin'] = '*'
  response['Cross-Origin-Opener-Policy'] = '*'
  return response

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
  user = request.user
  return Response({'username': user.username})

@api_view(['POST'])
def signup(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    user = User.objects.get(username=request.data['username'])
    user.set_password(request.data['password'])
    user.save()
    token = Token.objects.create(user=user)
    return Response({"token": token.key, "user": serializer.data})
  print(serializer.errors)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def guest_upload(request):
  try:
    data = request.data
    data._mutable = True
    data['owner'] = None
    
    # print(request.data)
    serializer = UploadSerializer(data=data)
    if serializer.is_valid():
      serializer.save()

      url_object = URL.objects.get(uid=serializer.data['url'])
      upload_object = url_object.upload
      filename = upload_object.filename

      bucket_name = 'fileflick'
      object_key = 'uploads/{}.{}'.format(serializer.data['url'],filename.split('.')[-1])
      download_url = generate_s3_download_url(bucket_name, object_key)
      # print(download_url)

      url_object.original_url = download_url
      url_object.save()

      return Response({'url': url_object.original_url, 'owner': serializer.data['owner'], 'filename': serializer.data['filename']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Exception as e:
    print(e)
    return Response({'url': 'Internal Server Error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_upload(request):
  try:
    request.data['owner'] = request.user.username
    # print(type(request.user))
    data = request.data
    # print(request.data)
    serializer = UploadSerializer(data=data)
    if serializer.is_valid():
      serializer.save()

      url_object = URL.objects.get(uid=serializer.data['url'])
      upload_object = url_object.upload
      filename = upload_object.filename

      bucket_name = 'file-flick'
      object_key = 'uploads/{}.{}'.format(serializer.data['url'],filename.split('.')[-1])
      download_url = generate_s3_download_url(bucket_name, object_key)
      # print(download_url)

      url_object.original_url = download_url
      url_object.save()

      return Response({'url': url_object.original_url, 'owner': serializer.data['owner'], 'filename': serializer.data['filename']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Exception as e:
    print(e)
    return Response({}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def recent(request):
  print(request.user)
  try:
    uploads = request.user.uploads
  except:
    uploads = []
  # print(request.user)
  serializer = UploadSerializer(uploads, many=True)
  return Response({"uploads": serializer.data})

@api_view(['GET'])
def download(request, shortuid):
  print(shortuid)
  url_object = URL.objects.get(short_uid=shortuid)
  if url_object is None:
    return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
  else:
    upload_object = url_object.upload
    filename = upload_object.filename

    bucket_name = 'file-flick'
    object_key = 'uploads/{}.{}'.format(url_object.uid,filename.split('.')[-1])
    content = get_s3_file(bucket_name, object_key)
    if content is not None:
      response = HttpResponse(content, content_type='application/octet-stream')
      response['Content-Disposition'] = f'attachment; filename="{filename}"'
      return response
    
    return HttpResponse("No AWS credentials found.", status=500)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_upload(request):
  try:
    # user = request.user
    uid = request.data['uid']

    url_object = URL.objects.get(uid=uid)
    upload_object = url_object.upload
    filename = upload_object.filename

    bucket_name = 'file-flick'
    object_key = 'uploads/{}.{}'.format(uid,filename.split('.')[-1])

    if delete_s3_object(bucket_name, object_key) :
      url_object.delete()
      upload_object.delete()
      return Response({'message': 'success'}, status=status.HTTP_200_OK)
    else:
      return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)

  except Exception as e:
    print(e)
    return Response({}, status=status.HTTP_503_SERVICE_UNAVAILABLE)