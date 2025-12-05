"""
Script para crear usuarios de prueba usando la API de producción
Ejecutar: python create_test_users_api.py
"""

import requests
import json

# URL de la API en producción
API_URL = "https://app-escolar-backend.onrender.com"

# Datos de administradores
administradores = [
    {
        "first_name": "Carlos",
        "last_name": "González Pérez",
        "email": "carlos.admin@escolar.com",
        "password": "admin123",
        "rol": "Admin",
        "clave_admin": "ADM001",
        "telefono": "5551234501",
        "rfc": "GOPC850101ABC",
        "edad": 35,
        "ocupacion": "Administrador"
    },
    {
        "first_name": "María",
        "last_name": "Rodríguez López",
        "email": "maria.admin@escolar.com",
        "password": "admin123",
        "rol": "Admin",
        "clave_admin": "ADM002",
        "telefono": "5551234502",
        "rfc": "ROLM900202DEF",
        "edad": 32,
        "ocupacion": "Administradora"
    },
    {
        "first_name": "José",
        "last_name": "Martínez Sánchez",
        "email": "jose.admin@escolar.com",
        "password": "admin123",
        "rol": "Admin",
        "clave_admin": "ADM003",
        "telefono": "5551234503",
        "rfc": "MASJ880303GHI",
        "edad": 38,
        "ocupacion": "Administrador"
    },
    {
        "first_name": "Ana",
        "last_name": "Fernández García",
        "email": "ana.admin@escolar.com",
        "password": "admin123",
        "rol": "Admin",
        "clave_admin": "ADM004",
        "telefono": "5551234504",
        "rfc": "FEGA920404JKL",
        "edad": 30,
        "ocupacion": "Administradora"
    },
    {
        "first_name": "Luis",
        "last_name": "Hernández Díaz",
        "email": "luis.admin@escolar.com",
        "password": "admin123",
        "rol": "Admin",
        "clave_admin": "ADM005",
        "telefono": "5551234505",
        "rfc": "HEDL870505MNO",
        "edad": 36,
        "ocupacion": "Administrador"
    }
]

# Datos de maestros
maestros = [
    {
        "first_name": "Roberto",
        "last_name": "Sánchez Ruiz",
        "email": "roberto.maestro@escolar.com",
        "password": "maestro123",
        "rol": "Maestro",
        "id_trabajador": "M001",
        "fecha_nacimiento": "1985-05-15",
        "telefono": "5552345601",
        "rfc": "SARR850515PQR",
        "cubiculo": "A-101",
        "area_investigacion": "Matemáticas Aplicadas",
        "materias_json": ["Álgebra", "Geometría", "Cálculo"]
    },
    {
        "first_name": "Laura",
        "last_name": "Torres Ramírez",
        "email": "laura.maestro@escolar.com",
        "password": "maestro123",
        "rol": "Maestro",
        "id_trabajador": "M002",
        "fecha_nacimiento": "1990-03-22",
        "telefono": "5552345602",
        "rfc": "TORL900322STU",
        "cubiculo": "B-205",
        "area_investigacion": "Biología y Química",
        "materias_json": ["Biología", "Química", "Física"]
    },
    {
        "first_name": "Pedro",
        "last_name": "Flores Morales",
        "email": "pedro.maestro@escolar.com",
        "password": "maestro123",
        "rol": "Maestro",
        "id_trabajador": "M003",
        "fecha_nacimiento": "1982-11-08",
        "telefono": "5552345603",
        "rfc": "FOMP821108VWX",
        "cubiculo": "C-310",
        "area_investigacion": "Historia de México",
        "materias_json": ["Historia", "Civismo", "Geografía"]
    },
    {
        "first_name": "Sofia",
        "last_name": "Jiménez Castro",
        "email": "sofia.maestro@escolar.com",
        "password": "maestro123",
        "rol": "Maestro",
        "id_trabajador": "M004",
        "fecha_nacimiento": "1988-07-19",
        "telefono": "5552345604",
        "rfc": "JICS880719YZA",
        "cubiculo": "D-102",
        "area_investigacion": "Literatura Mexicana",
        "materias_json": ["Español", "Literatura", "Redacción"]
    },
    {
        "first_name": "Miguel",
        "last_name": "Vargas Ortiz",
        "email": "miguel.maestro@escolar.com",
        "password": "maestro123",
        "rol": "Maestro",
        "id_trabajador": "M005",
        "fecha_nacimiento": "1986-09-25",
        "telefono": "5552345605",
        "rfc": "VAOM860925BCD",
        "cubiculo": "E-208",
        "area_investigacion": "Lenguas Extranjeras",
        "materias_json": ["Inglés", "Francés"]
    }
]

# Datos de alumnos
alumnos = [
    {
        "first_name": "Diego",
        "last_name": "Ramírez Cruz",
        "email": "diego.alumno@escolar.com",
        "password": "alumno123",
        "rol": "Alumno",
        "matricula": "A2025001",
        "curp": "RACD051215HDFRGG01",
        "rfc": "RACD051215ABC",
        "fecha_nacimiento": "2005-12-15",
        "edad": 18,
        "telefono": "5553456701",
        "ocupacion": "Estudiante"
    },
    {
        "first_name": "Valeria",
        "last_name": "Mendoza Silva",
        "email": "valeria.alumno@escolar.com",
        "password": "alumno123",
        "rol": "Alumno",
        "matricula": "A2025002",
        "curp": "MESV060408MDFNLL02",
        "rfc": "MESV060408DEF",
        "fecha_nacimiento": "2006-04-08",
        "edad": 17,
        "telefono": "5553456702",
        "ocupacion": "Estudiante"
    },
    {
        "first_name": "Andrés",
        "last_name": "Gutiérrez Reyes",
        "email": "andres.alumno@escolar.com",
        "password": "alumno123",
        "rol": "Alumno",
        "matricula": "A2025003",
        "curp": "GURA040320HDFTYN03",
        "rfc": "GURA040320GHI",
        "fecha_nacimiento": "2004-03-20",
        "edad": 19,
        "telefono": "5553456703",
        "ocupacion": "Estudiante"
    },
    {
        "first_name": "Camila",
        "last_name": "Moreno Rojas",
        "email": "camila.alumno@escolar.com",
        "password": "alumno123",
        "rol": "Alumno",
        "matricula": "A2025004",
        "curp": "MORC070511MDFRRM04",
        "rfc": "MORC070511JKL",
        "fecha_nacimiento": "2007-05-11",
        "edad": 16,
        "telefono": "5553456704",
        "ocupacion": "Estudiante"
    },
    {
        "first_name": "Daniel",
        "last_name": "Delgado Herrera",
        "email": "daniel.alumno@escolar.com",
        "password": "alumno123",
        "rol": "Alumno",
        "matricula": "A2025005",
        "curp": "DEHD060722HDFLRN05",
        "rfc": "DEHD060722MNO",
        "fecha_nacimiento": "2006-07-22",
        "edad": 17,
        "telefono": "5553456705",
        "ocupacion": "Estudiante"
    }
]

def crear_administradores():
    """Crear administradores vía API"""
    print("\n=== Creando Administradores ===")
    for admin in administradores:
        try:
            response = requests.post(f"{API_URL}/admin/", json=admin)
            if response.status_code in [200, 201]:
                print(f"✅ Creado: {admin['first_name']} {admin['last_name']} - {admin['email']}")
            else:
                print(f"❌ Error: {admin['email']} - {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Excepción: {admin['email']} - {str(e)}")

def crear_maestros():
    """Crear maestros vía API"""
    print("\n=== Creando Maestros ===")
    for maestro in maestros:
        try:
            response = requests.post(f"{API_URL}/maestros/", json=maestro)
            if response.status_code in [200, 201]:
                print(f"✅ Creado: {maestro['first_name']} {maestro['last_name']} - {maestro['area_investigacion']} - {maestro['email']}")
            else:
                print(f"❌ Error: {maestro['email']} - {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Excepción: {maestro['email']} - {str(e)}")

def crear_alumnos():
    """Crear alumnos vía API"""
    print("\n=== Creando Alumnos ===")
    for alumno in alumnos:
        try:
            response = requests.post(f"{API_URL}/alumnos/", json=alumno)
            if response.status_code in [200, 201]:
                print(f"✅ Creado: {alumno['first_name']} {alumno['last_name']} - {alumno['matricula']} - {alumno['email']}")
            else:
                print(f"❌ Error: {alumno['email']} - {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Excepción: {alumno['email']} - {str(e)}")

def main():
    """Función principal"""
    print("=" * 70)
    print("  SCRIPT DE CREACIÓN DE USUARIOS DE PRUEBA - APP ESCOLAR")
    print("  API: " + API_URL)
    print("=" * 70)
    
    print("\n⚠️  NOTA: El backend puede tardar 30-60 segundos en despertar si está inactivo...")
    print("⏳ Esperando respuesta del backend...")
    
    # Verificar que el backend esté activo
    try:
        response = requests.get(API_URL, timeout=90)
        if response.status_code == 200:
            print("✅ Backend activo y respondiendo\n")
        else:
            print(f"⚠️  Backend respondió con código {response.status_code}\n")
    except Exception as e:
        print(f"❌ Error conectando al backend: {str(e)}\n")
        print("Por favor verifica que el backend esté activo y vuelve a intentar.\n")
        return
    
    crear_administradores()
    crear_maestros()
    crear_alumnos()
    
    print("\n" + "=" * 70)
    print("  ✅ PROCESO COMPLETADO")
    print("=" * 70)
    
    print("\n🔑 CREDENCIALES DE PRUEBA:")
    print("   • Administradores: admin123")
    print("   • Maestros: maestro123")
    print("   • Alumnos: alumno123")
    print("\n")

if __name__ == '__main__':
    main()
