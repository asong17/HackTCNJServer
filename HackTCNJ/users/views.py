
from rest_framework.decorators import api_view
from message.models import Message
from message.serializers import MessageSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import AdminSerializer


@api_view(['GET'])
def see_unapproved(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if not user:
        return Response('Wrong username or password', status=status.HTTP_401_UNAUTHORIZED)

    user_serializer = AdminSerializer(data=request)

    if not user_serializer.check(user):
        return Response('Not Administrator', status=status.HTTP_401_UNAUTHORIZED)

    queryset = Message.objects.filter(approved=False, resolved=False)
    serializer = MessageSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def approve_message(request):

    username = request.data.get('username')
    password = request.data.get('password')
    message_id = request.data.get('message_id')

    user = authenticate(username=username, password=password)

    if not user:
        return Response('Wrong username or password', status=status.HTTP_401_UNAUTHORIZED)

    user_serializer = AdminSerializer(data=request)

    if not user_serializer.check(user):
        return Response('Not Administrator', status=status.HTTP_401_UNAUTHORIZED)

    message = Message.objects.get(id=message_id)
    user_serializer.approve(message)

    return Response('Approved', status=status.HTTP_200_OK)



