from django.conf.urls import url, include
from .controller import loginController,\
     classifierController ,\
     accountController,\
     homeController, \
     userController,\
     errorController



urlpatterns = [
    url(r'^$', loginController.do_login, name='login'),
    url(r'^logout', loginController.do_logout, name='logout'),
    url(r'^resetPass', loginController.resetPass, name='resetPass'),
    url(r'^register', loginController.register, name='register'),
    url(r'^account$', accountController.index, name='account'),
    url(r'^account/update', userController.password_change, name='account/update'),
    url(r'^account/profileUpdate', userController.change_data, name='account/profileUpdate'),
    url(r'^register/add', loginController.register,  name='account/add'),
    url(r'^home', homeController.home, name='home'),
    url(r'^user', userController.index, name='user'),
    url(r'^classifier$', classifierController.index, name='classifier'),
    url(r'^classifier/add', classifierController.add, name='add'),
    url(r'^classifier/delete', classifierController.removeClassifier, name='delete'),
    url(r'^classifier/getAllClassfiers', classifierController.getAllClassfiers, name='getAllClassfiers'),
    url(r'^classifier/getDisease', classifierController.getDisease, name='getDisease'),
]



handler404 = 'administrator.controller.errorController.page_not_found'

