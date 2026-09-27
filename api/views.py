from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Note


@api_view(['GET'])
def users(request):
    users = User.objects.all()

    data = []

    for user in users:
        data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

    return Response(data)


@api_view(['POST'])
def notes(request):
    user_id = request.data.get('user_id')
    text = request.data.get('text')

    if not user_id or not text:
        return Response(
            {'error': 'user_id и text обязательны'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {'error': 'Пользователь не найден'},
            status=status.HTTP_404_NOT_FOUND
        )

    Note.objects.create(
        user=user,
        text=text
    )

    return Response({
        'message': 'Заметка создана',
        'user_id': user.id,
        'text': text
    })