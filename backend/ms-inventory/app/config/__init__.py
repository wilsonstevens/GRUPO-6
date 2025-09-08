import os
from datetime import datetime

class Config:
    """Configuración base de la aplicación"""
    
    # Configuración de la base de datos SQLite
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "inventory.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de la aplicación
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Configuración de la aplicación
    JSON_SORT_KEYS = False
    
    # Configuración del servidor
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    HOST = '127.0.0.1'

class TestingConfig(Config):
    """Configuración para testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuración por defecto
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}