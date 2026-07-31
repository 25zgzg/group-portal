from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'home.html')


@api_view(['GET'])
@permission_classes([AllowAny])
def home_api_view(request):
    return Response({
        "project": "Портал групи",
        "description": "Ласкаво просимо на командний портал групи!",
        "modules": [
            "accounts",
            "announcements",
            "diary",
            "events",
            "forum",
            "gallery",
            "materials",
            "polls",
            "portfolio",
            "votes"
        ],
        "endpoints": {
            "auth_register": "/api/auth/register/",
            "auth_login": "/api/auth/login/",
            "auth_profile": "/api/auth/profile/"
        }
    })
