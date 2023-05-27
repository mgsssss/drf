from django.contrib.auth.models import User # User model
from django.contrib.auth.password_validation import validate_password # Django password 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token # Token model
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer): # 회원가입 serializer
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())], # Email validation
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password] # password validation
    )

    password2 = serializers.CharField( # Password 확인을 위한 필드
        write_only=True,
        required=True
    )

    class Meta:
        model=User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"}
            )
        return data
    
    def create(self, validated_data):
    # CREATE 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하게 함.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user