#!/usr/bin/env python3
"""
Punto de entrada del microservicio de inventario
"""

from app import create_app, init_db
import os

def main():
    """Función principal para ejecutar el microservicio"""
    
    # Crear la aplicación Flask
    app = create_app()
    
    # Inicializar la base de datos
    init_db(app)
    
    # Mostrar información del servicio
    print("=" * 60)
    print("🚀 MICROSERVICIO DE INVENTARIO INICIADO")
    print("=" * 60)
    print("📊 Servicio: ms-inventory")
    print("🌐 Host: 0.0.0.0")
    print("🔌 Puerto: 5000")
    print("📁 Base de datos: inventory.db")
    print("=" * 60)
    print("📋 ENDPOINTS DISPONIBLES:")
    print("=" * 60)
    print("POST   /api/inventory           - Crear registro")
    print("GET    /api/inventory           - Obtener todos los registros")
    print("GET    /api/inventory/<id>      - Obtener registro por ID")
    print("PUT    /api/inventory/<id>      - Actualizar registro")
    print("DELETE /api/inventory/<id>      - Eliminar registro")
    print("GET    /api/inventory/search    - Buscar registros")
    print("GET    /health                  - Estado del servicio")
    print("=" * 60)
    print("🔧 PARÁMETROS DE CONSULTA:")
    print("- country: Filtrar por país")
    print("- zone: Filtrar por zona")
    print("- product_id: Filtrar por producto")
    print("=" * 60)
    
    # Ejecutar la aplicación
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT']
    )

if __name__ == '__main__':
    main()