from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from webService.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer