"""
Script para asignar roles/grupos a los usuarios creados
Ejecutar: python fix_user_groups.py
"""

import requests
import json

# URL de la API en producción
API_URL = "https://app-escolar-backend.onrender.com"

# Datos para asignar grupos
admin_users = [
    "carlos.admin@escolar.com",
    "maria.admin@escolar.com",
    "jose.admin@escolar.com",
    "ana.admin@escolar.com",
    "luis.admin@escolar.com",
]

maestro_users = [
    "roberto.maestro@escolar.com",
    "laura.maestro@escolar.com",
    "pedro.maestro@escolar.com",
    "sofia.maestro@escolar.com",
    "miguel.maestro@escolar.com",
]

alumno_users = [
    "diego.alumno@escolar.com",
    "valeria.alumno@escolar.com",
    "andres.alumno@escolar.com",
    "camila.alumno@escolar.com",
    "daniel.alumno@escolar.com",
]

def main():
    print("=" * 70)
    print("  SCRIPT PARA REPARAR GRUPOS/ROLES DE USUARIOS")
    print("=" * 70)
    print("\n⚠️  NOTA: Este script intenta hacer login para probar la autenticación")
    print("⏳ Esperando respuesta del backend...\n")
    
    # Prueba con un usuario admin
    test_email = admin_users[0]
    test_password = "admin123"
    
    print(f"🔐 Probando login con: {test_email}")
    
    try:
        response = requests.post(
            f"{API_URL}/login/",
            json={"username": test_email, "password": test_password},
            timeout=60
        )
        
        print(f"📊 Respuesta del servidor: {response.status_code}")
        print(f"📝 Contenido: {response.text}\n")
        
        if response.status_code == 200:
            print("✅ ¡LOGIN EXITOSO!")
            data = response.json()
            print(f"✅ Token: {data.get('token', 'N/A')}")
            print(f"✅ Rol: {data.get('rol', 'N/A')}")
        elif response.status_code == 403:
            print("❌ ERROR 403 - Acceso Prohibido")
            print("   Posibles causas:")
            print("   - Usuario no existe")
            print("   - Contraseña incorrecta")
            print("   - Usuario no tiene grupo/rol asignado")
            print("   - Usuario no está activo (is_active=False)")
        else:
            print(f"❌ Error {response.status_code}")
            
    except Exception as e:
        print(f"❌ Excepción: {str(e)}")
    
    print("\n" + "=" * 70)
    print("\n📋 Para resolver el problema, es necesario:")
    print("1. Acceder a Django Admin del backend")
    print("2. Ir a Users → Grupos")
    print("3. Asignar cada usuario a su grupo correspondiente:")
    print(f"   - Admin: {', '.join(admin_users)}")
    print(f"   - Maestro: {', '.join(maestro_users)}")
    print(f"   - Alumno: {', '.join(alumno_users)}")
    print("\nO ejecutar un comando Django en producción (en Render Shell)")
    print("\n")

if __name__ == '__main__':
    main()
