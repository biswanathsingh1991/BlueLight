from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . models import TestModel
from . serializers import TestModelSerializer
# Create your views here.


class TestView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

class LikedBool(ListAPIView):
    pass
