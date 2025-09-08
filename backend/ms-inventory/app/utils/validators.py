class InventoryValidator:
    """Validador para datos de inventario"""
    
    REQUIRED_FIELDS_CREATE = ['country', 'zone', 'product_id', 'quantity']
    
    def validate_create_data(self, data):
        """Validar datos para crear inventario"""
        if not data:
            return {'valid': False, 'message': 'Datos requeridos'}
        
        # Validar campos requeridos
        for field in self.REQUIRED_FIELDS_CREATE:
            if field not in data:
                return {'valid': False, 'message': f'Campo requerido: {field}'}
        
        # Validar tipos de datos
        if not isinstance(data['country'], str) or not data['country'].strip():
            return {'valid': False, 'message': 'Country debe ser un string no vacío'}
        
        if not isinstance(data['zone'], str) or not data['zone'].strip():
            return {'valid': False, 'message': 'Zone debe ser un string no vacío'}
        
        if not isinstance(data['product_id'], str) or not data['product_id'].strip():
            return {'valid': False, 'message': 'Product_id debe ser un string no vacío'}
        
        # Validar quantity
        try:
            quantity = int(data['quantity'])
            if quantity < 0:
                return {'valid': False, 'message': 'La quantity debe ser un número positivo'}
        except (ValueError, TypeError):
            return {'valid': False, 'message': 'La quantity debe ser un número válido'}
        
        return {'valid': True}
    
    def validate_update_data(self, data):
        """Validar datos para actualizar inventario"""
        if not data:
            return {'valid': False, 'message': 'Datos requeridos para actualización'}
        
        # Validar que al menos un campo esté presente
        allowed_fields = ['country', 'zone', 'product_id', 'quantity']
        if not any(field in data for field in allowed_fields):
            return {'valid': False, 'message': 'Debe proporcionar al menos un campo para actualizar'}
        
        # Validar tipos de datos si están presentes
        if 'country' in data:
            if not isinstance(data['country'], str) or not data['country'].strip():
                return {'valid': False, 'message': 'Country debe ser un string no vacío'}
        
        if 'zone' in data:
            if not isinstance(data['zone'], str) or not data['zone'].strip():
                return {'valid': False, 'message': 'Zone debe ser un string no vacío'}
        
        if 'product_id' in data:
            if not isinstance(data['product_id'], str) or not data['product_id'].strip():
                return {'valid': False, 'message': 'Product_id debe ser un string no vacío'}
        
        if 'quantity' in data:
            try:
                quantity = int(data['quantity'])
                if quantity < 0:
                    return {'valid': False, 'message': 'La quantity debe ser un número positivo'}
            except (ValueError, TypeError):
                return {'valid': False, 'message': 'La quantity debe ser un número válido'}
        
        return {'valid': True}
    
    def validate_search_params(self, country=None, zone=None):
        """Validar parámetros de búsqueda"""
        if not country and not zone:
            return {'valid': False, 'message': 'Debe proporcionar al menos country o zone para buscar'}
        
        return {'valid': True}