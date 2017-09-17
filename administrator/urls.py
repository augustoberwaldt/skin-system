from django.conf.urls import url, include
from .controller import loginController,\
     classifierController ,\
     accountController


urlpatterns = [
    url(r'^$', loginController.login, name='login'),
    url(r'^logout', loginController.logout, name='logout'),
    url(r'^resetPass', loginController.resetPass, name='resetPass'),
    url(r'^register', loginController.register, name='register'),
    url(r'^account', accountController.index, name='account'),
    url(r'^home', loginController.home, name='home'),
    url(r'^classifier$', classifierController.index, name='classifier'),
    url(r'^classifier/add', classifierController.add, name='add'),
    url(r'^classifier/getDisease', classifierController.getDisease, name='getDisease'),
]

