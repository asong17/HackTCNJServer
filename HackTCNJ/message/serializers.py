from rest_framework import serializers
from .models import Message, School


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, school_id, content, urgent):

        new = Message(school_id=school_id, content=content, urgent=urgent, approved=False)
        new.save()
        return new




