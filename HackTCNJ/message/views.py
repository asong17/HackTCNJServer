
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MessageSerializer
from rest_framework.response import Response


@api_view(['POST'])
def post_message(request):

    school = request.data.get('school')
    content = request.data.get('content')
    urgent = request.data.get('urgent')

    serializer = MessageSerializer(data=request.data)

    if str(urgent) is 1:
        serializer.create(school=school, content=content, urgent=True)
    else:
        serializer.create(school=school, content=content, urgent=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


