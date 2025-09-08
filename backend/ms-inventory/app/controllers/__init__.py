from flask import request, jsonify
from app.services import InventoryService
from app.utils.validators import InventoryValidator
from app.utils import success_response, error_response

class InventoryController:
    """Controlador para manejar las peticiones HTTP del inventario"""
    
    def __init__(self):
        self.inventory_service = InventoryService()
        self.validator = InventoryValidator()
    
    def create_inventory(self):
        """Crear nuevo registro de inventario"""
        try:
            data = request.get_json()
            
            # Validar datos de entrada
            validation_result = self.validator.validate_create_data(data)
            if not validation_result['valid']:
                return error_response(validation_result['message'], 400)
            
            # Crear registro
            inventory = self.inventory_service.create_inventory(data)
            
            return success_response(
                'Registro de inventario creado exitosamente',
                inventory.to_dict(),
                201
            )
            
        except Exception as e:
            return error_response(f'Error al crear el registro: {str(e)}', 500)
    
    def get_all_inventory(self):
        """Obtener todos los registros de inventario con filtros"""
        try:
            # Parámetros de consulta
            country = request.args.get('country')
            zone = request.args.get('zone')
            product_id = request.args.get('product_id')
            
            # Obtener registros
            result = self.inventory_service.get_all_inventory(
                country=country,
                zone=zone,
                product_id=product_id
            )
            
            return success_response(
                'Registros obtenidos exitosamente',
                result['data'],
                {'total': result['total']}
            )
            
        except Exception as e:
            return error_response(f'Error al obtener los registros: {str(e)}', 500)
    
    def get_inventory_by_id(self, inventory_id):
        """Obtener un registro específico por ID"""
        try:
            inventory = self.inventory_service.get_inventory_by_id(inventory_id)
            if not inventory:
                return error_response('Registro no encontrado', 404)
            
            return success_response(
                'Registro obtenido exitosamente',
                inventory.to_dict()
            )
            
        except Exception as e:
            return error_response(f'Error al obtener el registro: {str(e)}', 500)
    
    def update_inventory(self, inventory_id):
        """Actualizar un registro existente"""
        try:
            data = request.get_json()
            
            # Validar datos de entrada
            validation_result = self.validator.validate_update_data(data)
            if not validation_result['valid']:
                return error_response(validation_result['message'], 400)
            
            # Actualizar registro
            inventory = self.inventory_service.update_inventory(inventory_id, data)
            if not inventory:
                return error_response('Registro no encontrado', 404)
            
            return success_response(
                'Registro de inventario actualizado exitosamente',
                inventory.to_dict()
            )
            
        except Exception as e:
            return error_response(f'Error al actualizar el registro: {str(e)}', 500)
    
    def delete_inventory(self, inventory_id):
        """Eliminar un registro"""
        try:
            success = self.inventory_service.delete_inventory(inventory_id)
            if not success:
                return error_response('Registro no encontrado', 404)
            
            return success_response(
                'Registro de inventario eliminado exitosamente',
                {'deleted_id': inventory_id}
            )
            
        except Exception as e:
            return error_response(f'Error al eliminar el registro: {str(e)}', 500)
    
    def search_inventory(self):
        """Buscar registros por país y/o zona"""
        try:
            country = request.args.get('country')
            zone = request.args.get('zone')
            
            if not country and not zone:
                return error_response('Debe proporcionar al menos country o zone para buscar', 400)
            
            results = self.inventory_service.search_inventory(country=country, zone=zone)
            
            return success_response(
                'Búsqueda completada exitosamente',
                results['data'],
                {'total_results': results['total_results']}
            )
            
        except Exception as e:
            return error_response(f'Error en la búsqueda: {str(e)}', 500)