from app.models import Inventory, db
from sqlalchemy import and_, or_
from datetime import datetime

class InventoryService:
    """Servicio para la lógica de negocio del inventario"""
    
    def create_inventory(self, data):
        """Crear nuevo registro de inventario"""
        inventory = Inventory.from_dict(data)
        db.session.add(inventory)
        db.session.commit()
        return inventory
    
    def get_all_inventory(self, country=None, zone=None, product_id=None):
        """Obtener todos los registros con filtros"""
        query = Inventory.query
        
        # Aplicar filtros
        if country:
            query = query.filter(Inventory.country.ilike(f'%{country}%'))
        if zone:
            query = query.filter(Inventory.zone.ilike(f'%{zone}%'))
        if product_id:
            query = query.filter(Inventory.product_id.ilike(f'%{product_id}%'))
        
        results = query.all()
        inventory_items = [item.to_dict() for item in results]
        
        return {
            'data': inventory_items,
            'total': len(inventory_items)
        }
    
    def get_inventory_by_id(self, inventory_id):
        """Obtener registro por ID"""
        return Inventory.query.get(inventory_id)
    
    def update_inventory(self, inventory_id, data):
        """Actualizar registro existente"""
        inventory = Inventory.query.get(inventory_id)
        if not inventory:
            return None
        
        inventory.update_from_dict(data)
        db.session.commit()
        return inventory
    
    def delete_inventory(self, inventory_id):
        """Eliminar registro"""
        inventory = Inventory.query.get(inventory_id)
        if not inventory:
            return False
        
        db.session.delete(inventory)
        db.session.commit()
        return True
    
    def search_inventory(self, country=None, zone=None):
        """Buscar registros por país y/o zona"""
        query = Inventory.query
        
        if country:
            query = query.filter(Inventory.country.ilike(f'%{country}%'))
        if zone:
            query = query.filter(Inventory.zone.ilike(f'%{zone}%'))
        
        results = query.all()
        inventory_items = [item.to_dict() for item in results]
        
        return {
            'data': inventory_items,
            'total_results': len(inventory_items)
        }
    
    def get_inventory_stats(self):
        """Obtener estadísticas del inventario"""
        total_records = Inventory.query.count()
        total_countries = db.session.query(Inventory.country).distinct().count()
        total_zones = db.session.query(Inventory.zone).distinct().count()
        total_products = db.session.query(Inventory.product_id).distinct().count()
        
        return {
            'total_records': total_records,
            'total_countries': total_countries,
            'total_zones': total_zones,
            'total_products': total_products
        }