from django.contrib import admin
from django.urls import path, include
from crud_user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('crud_user.urls')),
    
]