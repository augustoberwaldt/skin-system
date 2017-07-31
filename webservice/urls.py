from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from . import views


schema_view = get_swagger_view(title='API')

urlpatterns = [
    url(r'^$', schema_view),
]
