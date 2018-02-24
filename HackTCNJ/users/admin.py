from django.contrib import admin
from .models import AdminUser, Student

admin.site.register(AdminUser)
admin.site.register(Student)
