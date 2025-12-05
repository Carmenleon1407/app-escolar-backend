from django.db.models import *
from app_movil_escolar_api.serializers import *
from app_movil_escolar_api.models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import Group

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                        context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_active:
            # Obtener perfil y roles del usuario
            roles = user.groups.all()
            role_names = []
            
            # Verifico si el usuario tiene un perfil asociado
            for role in roles:
                role_names.append(role.name.lower())
            
            # Si el usuario no tiene grupo, asignarlo automáticamente
            if not role_names:
                # Verificar qué tipo de perfil tiene y asignarle el grupo correspondiente
                admin = Administradores.objects.filter(user=user).first()
                maestro = Maestros.objects.filter(user=user).first()
                alumno = Alumnos.objects.filter(user=user).first()
                
                if admin:
                    admin_group, _ = Group.objects.get_or_create(name='Admin')
                    user.groups.add(admin_group)
                    role_names = ['admin']
                elif maestro:
                    maestro_group, _ = Group.objects.get_or_create(name='Maestro')
                    user.groups.add(maestro_group)
                    role_names = ['maestro']
                elif alumno:
                    alumno_group, _ = Group.objects.get_or_create(name='Alumno')
                    user.groups.add(alumno_group)
                    role_names = ['alumno']
                else:
                    return Response({"details": "Usuario sin perfil asociado"}, 403)
            
            # Si solo es un rol específico asignamos el elemento 0
            if role_names:
                role_names = role_names[0]
            else:
                return Response({"details": "Usuario sin rol asignado"}, 403)
            
            # Esta función genera la clave dinámica (token) para iniciar sesión
            token, created = Token.objects.get_or_create(user=user)
            
            # Verificar que tipo de usuario quiere iniciar sesión
            
            if role_names == 'alumno':
                alumno = Alumnos.objects.filter(user=user).first()
                if alumno:
                    alumno = AlumnoSerializer(alumno).data
                    alumno["token"] = token.key
                    alumno["rol"] = "alumno"
                    return Response(alumno, 200)
                else:
                    return Response({"details": "Perfil de alumno no encontrado"}, 404)
                    
            elif role_names == 'maestro':
                maestro = Maestros.objects.filter(user=user).first()
                if maestro:
                    maestro = MaestroSerializer(maestro).data
                    maestro["token"] = token.key
                    maestro["rol"] = "maestro"
                    return Response(maestro, 200)
                else:
                    return Response({"details": "Perfil de maestro no encontrado"}, 404)
                    
            elif role_names == 'admin':
                user_data = UserSerializer(user, many=False).data
                user_data['token'] = token.key
                user_data["rol"] = "admin"
                return Response(user_data, 200)
            else:
                return Response({"details": f"Rol no reconocido: {role_names}"}, 403)
            
        return Response({}, status=status.HTTP_403_FORBIDDEN)

class Logout(generics.GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        print("logout")
        user = request.user
        print(str(user))
        if user.is_active:
            token = Token.objects.get(user=user)
            token.delete()

            return Response({'logout':True})


        return Response({'logout': False})
