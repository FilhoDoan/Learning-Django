from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from loginUser.models import User

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)