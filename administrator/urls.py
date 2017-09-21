from django.conf.urls import url, include
from .controller import loginController,\
     classifierController ,\
     accountController,\
     homeController


urlpatterns = [
    url(r'^$', loginController.do_login, name='login'),
    url(r'^logout', loginController.do_logout, name='logout'),
    url(r'^resetPass', loginController.resetPass, name='resetPass'),
    url(r'^register', loginController.register, name='register'),
    url(r'^account', accountController.index, name='account'),
    url(r'^register/add', loginController.register, name='account/add'),
    url(r'^home', homeController.home, name='home'),
    url(r'^classifier$', classifierController.index, name='classifier'),
    url(r'^classifier/add', classifierController.add, name='add'),
    url(r'^classifier/getDisease', classifierController.getDisease, name='getDisease'),
]

