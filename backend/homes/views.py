from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response Response
from rest_framework.permission import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Home
from .serializer import HomeSerializer
from django.contrib.auth.models import User
# Create your views here.
