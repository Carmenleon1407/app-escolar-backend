"""
Script para poblar la base de datos con usuarios de prueba
Ejecutar: python populate_users.py
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_movil_escolar_api.settings')
django.setup()

from app_movil_escolar_api.models import Administradores, Maestros, Alumnos
from app_movil_escolar_api.cypher_utils import cipher_password

def crear_administradores():
    """Crear 5 administradores de prueba"""
    administradores = [
        {
            'nombre': 'Carlos',
            'apellidos': 'González Pérez',
            'correo_electronico': 'carlos.admin@escolar.com',
            'contraseña': 'admin123'
        },
        {
            'nombre': 'María',
            'apellidos': 'Rodríguez López',
            'correo_electronico': 'maria.admin@escolar.com',
            'contraseña': 'admin123'
        },
        {
            'nombre': 'José',
            'apellidos': 'Martínez Sánchez',
            'correo_electronico': 'jose.admin@escolar.com',
            'contraseña': 'admin123'
        },
        {
            'nombre': 'Ana',
            'apellidos': 'Fernández García',
            'correo_electronico': 'ana.admin@escolar.com',
            'contraseña': 'admin123'
        },
        {
            'nombre': 'Luis',
            'apellidos': 'Hernández Díaz',
            'correo_electronico': 'luis.admin@escolar.com',
            'contraseña': 'admin123'
        }
    ]
    
    print("\n=== Creando Administradores ===")
    for admin_data in administradores:
        # Verificar si ya existe
        if Administradores.objects.filter(correo_electronico=admin_data['correo_electronico']).exists():
            print(f"❌ Ya existe: {admin_data['correo_electronico']}")
            continue
        
        # Encriptar contraseña
        password_encrypted = cipher_password(admin_data['contraseña'])
        
        # Crear administrador
        admin = Administradores.objects.create(
            nombre=admin_data['nombre'],
            apellidos=admin_data['apellidos'],
            correo_electronico=admin_data['correo_electronico'],
            contraseña=password_encrypted
        )
        print(f"✅ Creado: {admin.nombre} {admin.apellidos} - {admin.correo_electronico}")

def crear_maestros():
    """Crear 5 maestros de prueba"""
    maestros = [
        {
            'nombre': 'Roberto',
            'apellidos': 'Sánchez Ruiz',
            'correo_electronico': 'roberto.maestro@escolar.com',
            'contraseña': 'maestro123',
            'especialidad': 'Matemáticas'
        },
        {
            'nombre': 'Laura',
            'apellidos': 'Torres Ramírez',
            'correo_electronico': 'laura.maestro@escolar.com',
            'contraseña': 'maestro123',
            'especialidad': 'Ciencias Naturales'
        },
        {
            'nombre': 'Pedro',
            'apellidos': 'Flores Morales',
            'correo_electronico': 'pedro.maestro@escolar.com',
            'contraseña': 'maestro123',
            'especialidad': 'Historia'
        },
        {
            'nombre': 'Sofia',
            'apellidos': 'Jiménez Castro',
            'correo_electronico': 'sofia.maestro@escolar.com',
            'contraseña': 'maestro123',
            'especialidad': 'Español'
        },
        {
            'nombre': 'Miguel',
            'apellidos': 'Vargas Ortiz',
            'correo_electronico': 'miguel.maestro@escolar.com',
            'contraseña': 'maestro123',
            'especialidad': 'Inglés'
        }
    ]
    
    print("\n=== Creando Maestros ===")
    for maestro_data in maestros:
        # Verificar si ya existe
        if Maestros.objects.filter(correo_electronico=maestro_data['correo_electronico']).exists():
            print(f"❌ Ya existe: {maestro_data['correo_electronico']}")
            continue
        
        # Encriptar contraseña
        password_encrypted = cipher_password(maestro_data['contraseña'])
        
        # Crear maestro
        maestro = Maestros.objects.create(
            nombre=maestro_data['nombre'],
            apellidos=maestro_data['apellidos'],
            correo_electronico=maestro_data['correo_electronico'],
            contraseña=password_encrypted,
            especialidad=maestro_data['especialidad']
        )
        print(f"✅ Creado: {maestro.nombre} {maestro.apellidos} - {maestro.especialidad} - {maestro.correo_electronico}")

def crear_alumnos():
    """Crear 5 alumnos de prueba"""
    alumnos = [
        {
            'nombre': 'Diego',
            'apellidos': 'Ramírez Cruz',
            'correo_electronico': 'diego.alumno@escolar.com',
            'contraseña': 'alumno123',
            'matricula': 'A2025001',
            'grado': '1° Secundaria'
        },
        {
            'nombre': 'Valeria',
            'apellidos': 'Mendoza Silva',
            'correo_electronico': 'valeria.alumno@escolar.com',
            'contraseña': 'alumno123',
            'matricula': 'A2025002',
            'grado': '2° Secundaria'
        },
        {
            'nombre': 'Andrés',
            'apellidos': 'Gutiérrez Reyes',
            'correo_electronico': 'andres.alumno@escolar.com',
            'contraseña': 'alumno123',
            'matricula': 'A2025003',
            'grado': '3° Secundaria'
        },
        {
            'nombre': 'Camila',
            'apellidos': 'Moreno Rojas',
            'correo_electronico': 'camila.alumno@escolar.com',
            'contraseña': 'alumno123',
            'matricula': 'A2025004',
            'grado': '1° Secundaria'
        },
        {
            'nombre': 'Daniel',
            'apellidos': 'Delgado Herrera',
            'correo_electronico': 'daniel.alumno@escolar.com',
            'contraseña': 'alumno123',
            'matricula': 'A2025005',
            'grado': '2° Secundaria'
        }
    ]
    
    print("\n=== Creando Alumnos ===")
    for alumno_data in alumnos:
        # Verificar si ya existe
        if Alumnos.objects.filter(correo_electronico=alumno_data['correo_electronico']).exists():
            print(f"❌ Ya existe: {alumno_data['correo_electronico']}")
            continue
        
        # Encriptar contraseña
        password_encrypted = cipher_password(alumno_data['contraseña'])
        
        # Crear alumno
        alumno = Alumnos.objects.create(
            nombre=alumno_data['nombre'],
            apellidos=alumno_data['apellidos'],
            correo_electronico=alumno_data['correo_electronico'],
            contraseña=password_encrypted,
            matricula=alumno_data['matricula'],
            grado=alumno_data['grado']
        )
        print(f"✅ Creado: {alumno.nombre} {alumno.apellidos} - {alumno.matricula} - {alumno.grado} - {alumno.correo_electronico}")

def main():
    """Función principal"""
    print("=" * 60)
    print("  SCRIPT DE POBLACIÓN DE USUARIOS - APP ESCOLAR")
    print("=" * 60)
    
    try:
        crear_administradores()
        crear_maestros()
        crear_alumnos()
        
        print("\n" + "=" * 60)
        print("  ✅ PROCESO COMPLETADO EXITOSAMENTE")
        print("=" * 60)
        
        # Mostrar resumen
        total_admins = Administradores.objects.count()
        total_maestros = Maestros.objects.count()
        total_alumnos = Alumnos.objects.count()
        
        print("\n📊 RESUMEN DE USUARIOS EN LA BASE DE DATOS:")
        print(f"   • Administradores: {total_admins}")
        print(f"   • Maestros: {total_maestros}")
        print(f"   • Alumnos: {total_alumnos}")
        print(f"   • TOTAL: {total_admins + total_maestros + total_alumnos}")
        
        print("\n🔑 CONTRASEÑAS DE PRUEBA:")
        print("   • Administradores: admin123")
        print("   • Maestros: maestro123")
        print("   • Alumnos: alumno123")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
