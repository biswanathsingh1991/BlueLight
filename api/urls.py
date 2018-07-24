from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . views import TestView

app_name = 'api'

urlpatterns = [
    path('test/', TestView.as_view(), name='test')
]
