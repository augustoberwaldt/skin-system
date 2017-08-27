from django.conf.urls import url, include
from .controller import loginController, classifierController;

urlpatterns = [
    url(r'^$', loginController.login, name='login'),
    url(r'^resetPass', loginController.resetPass, name='resetPass'),
    url(r'^register', loginController.register, name='register'),
    url(r'^home/', loginController.home , name='home'),
    url(r'^classifier/', classifierController.index , name='classifier'),
]

