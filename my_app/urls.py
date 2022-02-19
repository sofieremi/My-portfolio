from django.contrib import admin
from django.urls import path, include

from my_app.views import index

urlpatterns = [
    path('', index)
]