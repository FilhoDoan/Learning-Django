from django.shortcuts import render
from .models import usuarios
from django.http import HttpResponse

def homepage(request):
    return render(request,'crud_user/pages/user_list.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        
        usuarios.objects.create(username = username, passwd = passwd)
        user_dict = usuarios.objects.all()
        return render(request,'crud_user/pages/user_list.html', {'user_dict': user_dict}) 
    return render(request,'crud_user/pages/register_user.html')



    
    
    
    
    