from rest_framework import serializers
from base.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'bio')


class ProjectSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(many=False)

    class Meta:
        model = Project
        fields = '__all__'


class TaskStatusSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True)

    class Meta:
        model = TaskStatus
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
