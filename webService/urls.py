from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views.UserViewSet import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


schema_view = get_swagger_view(title='API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
]

