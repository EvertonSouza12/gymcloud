from django.urls import path
from . import views


urlpatterns = [
    path('gymcloud/login', views.login, name='gymcloud-login'),
    path('gymcloud/register', views.register, name='gymcloud-register'),
]