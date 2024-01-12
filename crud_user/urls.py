from django.urls import path
from crud_user import views

urlpatterns = [
    path('', views.register_user, name='register_user'),
]