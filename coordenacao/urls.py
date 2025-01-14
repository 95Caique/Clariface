
from django.contrib import admin
from django.urls import path, include
import register.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(register.urls)),
]
