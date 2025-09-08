from flask import Flask
from app.config import config
from app.models import db
from app.controllers import InventoryController
from app.utils import health_response
from flask import jsonify

def create_app(config_name='default'):
    """Factory function para crear la aplicación Flask"""
    app = Flask(__name__)
    
    # Configurar la aplicación
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Crear controlador
    inventory_controller = InventoryController()
    
    # Registrar rutas
    register_routes(app, inventory_controller)
    
    # Registrar manejadores de errores
    register_error_handlers(app)
    
    return app

def register_routes(app, inventory_controller):
    """Registrar todas las rutas de la aplicación"""
    
    # Rutas de inventario
    app.add_url_rule('/api/inventory', 'create_inventory', 
                     inventory_controller.create_inventory, methods=['POST'])
    
    app.add_url_rule('/api/inventory', 'get_all_inventory', 
                     inventory_controller.get_all_inventory, methods=['GET'])
    
    app.add_url_rule('/api/inventory/<int:inventory_id>', 'get_inventory_by_id', 
                     inventory_controller.get_inventory_by_id, methods=['GET'])
    
    app.add_url_rule('/api/inventory/<int:inventory_id>', 'update_inventory', 
                     inventory_controller.update_inventory, methods=['PUT'])
    
    app.add_url_rule('/api/inventory/<int:inventory_id>', 'delete_inventory', 
                     inventory_controller.delete_inventory, methods=['DELETE'])
    
    app.add_url_rule('/api/inventory/search', 'search_inventory', 
                     inventory_controller.search_inventory, methods=['GET'])
    
    # Ruta de salud
    app.add_url_rule('/health', 'health_check', 
                     lambda: health_response(), methods=['GET'])

def register_error_handlers(app):
    """Registrar manejadores de errores globales"""
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 'Recurso no encontrado',
            'timestamp': '2024-01-01T00:00:00'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor',
            'timestamp': '2024-01-01T00:00:00'
        }), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 'Solicitud incorrecta',
            'timestamp': '2024-01-01T00:00:00'
        }), 400

def init_db(app):
    """Inicializar la base de datos"""
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada correctamente")