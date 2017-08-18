from django.conf.urls import url, include
from . import views;

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^resetPass', views.resetPass, name='resetPass'),
    url(r'^register', views.register, name='register'),
    url(r'^home/', views.home , name='home'),
]

