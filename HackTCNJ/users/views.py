
from rest_framework.decorators import api_view
from message.models import Message
from message.serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminSerializer, StudentSerializer


@api_view(['GET'])
def see_unapproved(request):

    if request.method == 'GET':
        queryset = Message.objects.filter(approved=False, resolved=False)
        serializer = MessageSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def approve_message(request):

    # username = request.data.get('username')
    # password = request.data.get('password')
    message_id = request.data.get('message_id')

    if request.method == 'PUT':
        user_serializer = AdminSerializer()

        """
        if not user_serializer.login(username=username, password=password):
            return Response('Not Administrator', status=status.HTTP_401_UNAUTHORIZED)
        """

        message = Message.objects.get(id=message_id)
        user_serializer.approve(message)

        return Response('Approved', status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
def login_student(request):

    student_id = request.data.get('student_id')
    password = request.data.get('password')

    if request.method == 'PUT':
        serializer = StudentSerializer()

        if serializer.login(student_id=student_id, password=password):
            return Response('Login Success', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Not Authenticated', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def login_admin(request):

    name = request.data.get('name')
    password = request.data.get('password')

    if request.method == 'PUT':
        serializer = AdminSerializer()

        if request.method == 'PUT':
            if serializer.login(name=name, password=password):
                return Response('Login Success', status=status.HTTP_202_ACCEPTED)
            else:
                return Response('Not Authenticated', status=status.HTTP_401_UNAUTHORIZED)




