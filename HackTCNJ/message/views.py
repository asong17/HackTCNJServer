
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MessageSerializer
from rest_framework.response import Response
from .models import School


@api_view(['POST'])
def post_message(request):

    # school = request.data.get('school')
    content = request.data.get('content')
    urgent = request.data.get('urgent')

    """
    try:
        school_id = School.objects.get(title=school).id
    except School.DoesNotExist:
        return Response('School Does Not Exist', status=status.HTTP_404_NOT_FOUND)
        
    """

    if request.method == 'POST':
        school_id = 1

        serializer = MessageSerializer()

        serializer.create(school_id=school_id, content=content, urgent=urgent)

        return Response('Success', status=status.HTTP_202_ACCEPTED)



