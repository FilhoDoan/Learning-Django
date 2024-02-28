from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from loginUser.models import User
from rest_framework import status

@api_view(['GET','POST','PUT'])
def UserMethods(request,):
    if request.method == 'GET':        
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'PUT':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 
            
    