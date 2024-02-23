from rest_framework import serializers
from loginUser.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'