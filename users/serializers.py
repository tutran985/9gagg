from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
import re
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework.exceptions import ParseError

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password", "date_joined")

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        # del validated_data["confirm_password"]
        # return super(UserRegistrationSerializer, self).create(validated_data)

    def validate_email(self, value):
        if not re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", value):
            raise ParseError({"error_code":"400_EMAIL","message":"mail k dung dinh dang"})
        
        try:
            email = User.objects.get(email=value)
        except ObjectDoesNotExist:
            email = None
        
        if email:
            raise ParseError({"error_code":"400_EMAIL_EXIST","message":"mail da ton tai"})
        return value

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise ParseError({"error_code":"400_PASSWORD","message":"2 mat khau khong giong nhau"})
        return attrs


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise ParseError({
                    "error_code":"400_INACTIVE_ACCOUNT",
                    "message":self.default_error_messages['inactive_account'],
                })
            return attrs
        else:
            raise ParseError({
                "error_code":"400_INVALID_CREDENTIALS",
                "message":self.default_error_messages['invalid_credentials'],
            })


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token", "created")