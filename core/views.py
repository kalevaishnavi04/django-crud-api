from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserProfile
from .serializers import UserProfileSerializer

@api_view(['GET'])
def get_users(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_user(request, id):
    user = UserProfile.objects.get(id=id)
    serializer = UserProfileSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_user(request, id):
    user = UserProfile.objects.get(id=id)
    user.delete()
    return Response({"message": "User deleted successfully"})