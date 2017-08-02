from webService.models.UserModel import User
from rest_framework import routers, serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

