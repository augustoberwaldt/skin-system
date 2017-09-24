
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app/', include('administrator.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)