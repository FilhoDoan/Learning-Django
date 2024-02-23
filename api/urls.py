from django.urls import path
from . import views


urlpatterns = [
    path('',views.getUser),    
    path('add/',views.postUser)    
]
