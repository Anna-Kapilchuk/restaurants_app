from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator
from restaurants_app.models import Profile


class UserSerializer(ModelSerializer):

    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)
    address = serializers.CharField(required=True, max_length=256, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'address', 'profile']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'read_only': True}
        }
        validators = [UniqueTogetherValidator(User.objects.all(), ['email'])]
        depth = 1

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                        username=validated_data['email'],
                        email=validated_data['email'],
                        password=validated_data['password'],
                        first_name=validated_data.get('first_name', ''),
                        last_name=validated_data.get('last_name', ''))
            Profile.objects.create(user=user, address=validated_data['address'])

            return user


class UserProfileSerializer(ModelSerializer):

    def to_representation(self, instance):
        user_repr = super().to_representation(instance)
        user_repr['address'] = instance.profile.address
        user_repr['img_url'] = instance.profile.img_url
        return user_repr

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']


class DetailedUserSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = '__all__'
        model = Profile
