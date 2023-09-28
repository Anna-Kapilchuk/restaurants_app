
import os
import uuid
from django.contrib.auth.models import User
from django.http import JsonResponse
from google.auth.transport import requests
from google.cloud import storage
from google.oauth2 import id_token, service_account
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from restaurants_app.models import Profile
from restaurants_app.serializer.auth import UserProfileSerializer, UserSerializer


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': user.profile.address
        }
        return JsonResponse(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):

    serializer_class = UserProfileSerializer
    user_serializer = serializer_class(instance=request.user, many=False, context={'request': request})
    return Response(data=user_serializer.data)


@api_view(['POST'])
def google_login(request):
    google_jwt = request.data['google_jwt']
    CLIENT_ID = '582224161241-pcdsbikpfg3111ft3hi4q8ivtr6s1c4r.apps.googleusercontent.com'
    try:
        idinfo = id_token.verify_oauth2_token(google_jwt, requests.Request(), CLIENT_ID)
        print('idinfo from google:', idinfo)

        email = idinfo['email']
        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            print('does not exist')
            user = User.objects.create_user(username=email, email=email, password=str(uuid.uuid4()),
                                            first_name=idinfo['given_name'],
                                            last_name=idinfo['family_name'])
            Profile.objects.create(user=user, address='', img_url=idinfo['picture'])

        refresh = RefreshToken.for_user(user)
        return Response(data={
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

        print(idinfo)
    except ValueError as e:
        print(e)
    print(google_jwt)
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_img(request):

    bucket_name = 'restaurant-jb'
    file_stream = request.FILES['file'].file
    _, ext = os.path.splitext(request.FILES['file'].name)

    object_name = f"profile_img_{uuid.uuid4()}{ext}"

    credentials = service_account.Credentials.from_service_account_file(
        "C:\\Users\\Anna Kapilchuk\\keys\\restaurant-400212-a28167509acf.json")

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_file(file_stream)

    request.user.profile.img_url = blob.public_url
    request.user.profile.save()

    userSerializer = UserProfileSerializer(request.user)
    return Response(userSerializer.data)


