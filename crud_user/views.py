from django.shortcuts import render
from .models import usuarios

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        
        usuarios.objects.create(username = username, passwd = passwd)

        # usuarios_funcao.save()
        
        user_dict = usuarios.objects.all()
        
        return render(request,'template_crud_user/user_list.html', {'user_dict': user_dict})
    return render(request,'template_crud_user/homepage.html')

def get_all_user(request):
    ...
    
    
    
    
    