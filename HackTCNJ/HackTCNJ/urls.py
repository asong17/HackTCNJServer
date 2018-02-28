
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', include('message.urls')),
    path('users/', include('users.urls'))
]
