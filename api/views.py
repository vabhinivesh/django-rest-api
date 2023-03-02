from .response_handler import *
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def api_overview(request):
    api_urls = {

    }
    return handle_success(api_urls)


@api_view(['GET'])
def health_check(request):
    return handle_success(data={'status': 'Application is working fine'})


@api_view(['GET'])
def get_users_list(request):
    user = UserProfile.objects.all()
    serializer = UserProfileSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_data(request, pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    print(request.data)

    user_profile = UserProfileSerializer(data=request.data)
    user_main = UserSerializer(data=request.data)
    if user_main.is_valid():
        user_main.save()
        if user_profile.is_valid():
            user_profile.user = user_main
            user_profile.save()
        else:
            return handle_error(400)
    else:
        return handle_error(400)
    return handle_success(user_profile)


@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
