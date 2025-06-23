from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import PublicSerializer, UserSerializer
from .tasks import send_welcome_email

@api_view(['GET'])
def public_view(request):
    return Response({"message": "This is a public endpoint"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response(UserSerializer(request.user).data)

@api_view(['POST'])
def register_user(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    user = User.objects.create_user(username=username, email=email, password=password)
    send_welcome_email.delay(email)
    return Response({"message": f"User {username} created"})
