from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gymcloud-home'),
    path('gymcloud/login', views.login, name='gymcloud-login'),
    path('gymcloud/register', views.register, name='gymcloud-register'),
    path('gymcloud/setings/acount', views.setings, name='gymcloud-setings'),
    path('gymcloud/workouts/list', views.workouts, name='gymcloud-list-workouts'),
    path('gymcloud/workouts/setings/manage/workouts', views.manage_workouts, name='gymcloud-manage-workouts'),
]