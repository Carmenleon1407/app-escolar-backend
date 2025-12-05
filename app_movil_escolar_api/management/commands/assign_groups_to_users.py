"""
Management command para asignar grupos a usuarios
Uso: python manage.py assign_groups_to_users
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from app_movil_escolar_api.models import Administradores, Maestros, Alumnos

class Command(BaseCommand):
    help = 'Asigna grupos a usuarios según su tipo (Admin, Maestro, Alumno)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write(self.style.SUCCESS('  ASIGNANDO GRUPOS A USUARIOS'))
        self.stdout.write(self.style.SUCCESS('=' * 70))
        
        # Crear grupos si no existen
        admin_group, created = Group.objects.get_or_create(name='Admin')
        maestro_group, created = Group.objects.get_or_create(name='Maestro')
        alumno_group, created = Group.objects.get_or_create(name='Alumno')
        
        self.stdout.write('\n✅ Grupos creados/verificados:')
        self.stdout.write(f'   - Admin')
        self.stdout.write(f'   - Maestro')
        self.stdout.write(f'   - Alumno')
        
        # Asignar grupos a administradores
        self.stdout.write('\n=== Asignando Administradores ===')
        admins = Administradores.objects.all()
        for admin in admins:
            admin.user.groups.clear()
            admin.user.groups.add(admin_group)
            self.stdout.write(f'✅ {admin.user.email} → Admin')
        
        # Asignar grupos a maestros
        self.stdout.write('\n=== Asignando Maestros ===')
        maestros = Maestros.objects.all()
        for maestro in maestros:
            maestro.user.groups.clear()
            maestro.user.groups.add(maestro_group)
            self.stdout.write(f'✅ {maestro.user.email} → Maestro')
        
        # Asignar grupos a alumnos
        self.stdout.write('\n=== Asignando Alumnos ===')
        alumnos = Alumnos.objects.all()
        for alumno in alumnos:
            alumno.user.groups.clear()
            alumno.user.groups.add(alumno_group)
            self.stdout.write(f'✅ {alumno.user.email} → Alumno')
        
        self.stdout.write('\n' + '=' * 70)
        self.stdout.write(self.style.SUCCESS('✅ PROCESO COMPLETADO'))
        self.stdout.write('=' * 70 + '\n')
