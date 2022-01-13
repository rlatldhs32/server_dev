# login/serializer.py

from rest_framework import serializers
from .models import LoginUser
from django.contrib.auth.hashers import make_password


class LoginUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user_pw'] = make_password(validated_data['user_pw'])
        user = LoginUser.objects.create(**validated_data) #객체 만드는거 동일,직렬화된 데이터 들어감
        return user

    def validate(self, attrs):
        return attrs

    class Meta:
        model = LoginUser
        fields = ('user_id', 'user_pw', 'birth_day', 'gender', 'email', 'name', 'age')
