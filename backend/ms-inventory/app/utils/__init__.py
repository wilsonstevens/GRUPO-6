from flask import jsonify
from datetime import datetime

def success_response(message, data=None, status_code=200, **kwargs):
    """Crear respuesta de éxito estandarizada"""
    response = {
        'success': True,
        'message': message,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    if data is not None:
        response['data'] = data
    
    # Agregar campos adicionales (como paginación)
    for key, value in kwargs.items():
        response[key] = value
    
    return jsonify(response), status_code

def error_response(message, status_code=400, details=None):
    """Crear respuesta de error estandarizada"""
    response = {
        'success': False,
        'error': message,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    if details:
        response['details'] = details
    
    return jsonify(response), status_code

def health_response():
    """Crear respuesta de salud del servicio"""
    return success_response(
        'Servicio funcionando correctamente',
        {
            'status': 'healthy',
            'service': 'ms-inventory',
            'version': '1.0.0'
        }
    )