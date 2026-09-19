from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'required': True},
            'password': {'required': True, 'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': False},
            'phone_number': {'required': False},
        }

    # checking if either email or phone number exists
    def validate(self, attrs):
        email = attrs.get('email')
        phone_number = attrs.get('phone_number')
        if not email and not phone_number:
            raise serializers.ValidationError(
                'Either email or phone number is required.'
            )
        return attrs

    # hashing the password
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'email': {'read_only': True},
            'phone_number': {'read_only': True},
        }