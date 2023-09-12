from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restaurants_app.serializer.auth import SignupSerializer, UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(data=serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):

    serializer = UserSerializer(instance=request.user)
    return Response(data=serializer.data)

    # request.user.is_authenticated
