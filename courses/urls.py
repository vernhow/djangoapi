#removed the admin url import
from django.urls import path, include
from . import views
from rest_framework import routers #allows to POST and GET request

router = routers.DefaultRouter()
router.register ('courses', views.CourseView)

urlpatterns = [
    path ('', include(router.urls)), #include index page
]
