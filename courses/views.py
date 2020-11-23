from django.shortcuts import render
from rest_framework import viewsets #sets of pages to create
from .models import Course
from .serializers import CourseSerializer
# Create your views here.

class CourseView (viewsets.ModelViewSet):
    queryset = Course.objects.all() #pull all of the data from database
    serializer_class = CourseSerializer #assigned from serializers.py
