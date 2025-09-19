#!/usr/bin/env python3
"""
Main URL configuration for messaging_app project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),
]
