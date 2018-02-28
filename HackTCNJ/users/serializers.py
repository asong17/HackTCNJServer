from rest_framework import serializers
from .models import Student, AdminUser
from rest_framework.validators import UniqueValidator


class AdminSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True,
                                 max_length=32,
                                 validators=[UniqueValidator(queryset=Student.objects.all())]
                                 )

    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = AdminUser
        fields = '__all__'

    def approve(self, message):
        message.approved = True
        message.save()
        return True

    def check(self, user):
        if AdminUser.objects.filter(id=user.id).exist():
            return True
        else:
            return False

    def login(self, name, password):
        if AdminUser.objects.filter(name=name, password=password).exists():
            return True
        return False


class StudentSerializer(serializers.ModelSerializer):

    student_id = serializers.CharField(required=True,
                                       max_length=32,
                                       validators=[UniqueValidator(queryset=Student.objects.all())]
                                       )

    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = Student.objects.create_user(validated_data['username'],
                                           validated_data['email'],
                                           validated_data['password'])

        return user

    class Meta:
        model = Student
        fields = ('id', 'name', 'password')

    def login(self, student_id, password):
        if Student.objects.filter(student_id=student_id, password=password).exists():
            return True
        return False





