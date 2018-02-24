from rest_framework import serializers
from .models import Message, School


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, school, content, urgent):

        new = Message(school=school, content=content, urgent=urgent, approved=False)
        new.save()
        return new




