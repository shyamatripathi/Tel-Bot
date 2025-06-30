from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_welcome_email

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    
    # 👇 Call Celery task after successful registration
    send_welcome_email.delay(user.email)

    return Response({'message': 'User registered successfully!'})
