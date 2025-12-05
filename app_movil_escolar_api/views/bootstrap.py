import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class VersionView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        version = getattr(settings, "APP_VERSION", os.getenv("APP_VERSION", "1.0.0"))
        return Response({"version": version})

class APIRootView(APIView):
    """
    Vista raíz de la API que muestra información del backend
    """
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            "mensaje": "Bienvenido a App Escolar API",
            "version": "1.0.0",
            "estado": "Activo",
            "descripcion": "Sistema de gestión de eventos académicos",
            "endpoints": {
                "autenticacion": {
                    "login": "/login/",
                    "logout": "/logout/"
                },
                "usuarios": {
                    "administradores": "/admin/",
                    "lista_administradores": "/lista-admins/",
                    "total_usuarios": "/total-usuarios/"
                },
                "maestros": {
                    "crear_listar": "/maestros/",
                    "detalle": "/maestros/{id}/",
                    "lista_todos": "/lista-maestros/"
                },
                "alumnos": {
                    "crear_listar": "/alumnos/",
                    "detalle": "/alumnos/{id}/",
                    "lista_todos": "/lista-alumnos/"
                }
            },
            "frontend": "https://app-escolar-front1.vercel.app",
            "github": {
                "frontend": "https://github.com/Carmenleon1407/app-escolar-webapp",
                "backend": "https://github.com/Carmenleon1407/app-escolar-backend"
            },
            "tecnologias": ["Django 5.0", "Django REST Framework", "PostgreSQL", "Gunicorn"],
            "desarrollado_por": "Carmen León"
        })
