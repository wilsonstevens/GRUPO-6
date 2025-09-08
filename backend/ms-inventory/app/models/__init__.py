from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicialización de SQLAlchemy
db = SQLAlchemy()

class Inventory(db.Model):
    """Modelo para la entidad Inventory"""
    
    __tablename__ = 'inventory'
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    zone = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Inventory {self.id}: {self.product_id} in {self.country}-{self.zone}>'
    
    def to_dict(self):
        """Convierte el modelo a diccionario"""
        return {
            'id': self.id,
            'country': self.country,
            'zone': self.zone,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea una instancia del modelo desde un diccionario"""
        return cls(
            country=data.get('country'),
            zone=data.get('zone'),
            product_id=data.get('product_id'),
            quantity=data.get('quantity')
        )
    
    def update_from_dict(self, data):
        """Actualiza la instancia desde un diccionario"""
        if 'country' in data:
            self.country = data['country']
        if 'zone' in data:
            self.zone = data['zone']
        if 'product_id' in data:
            self.product_id = data['product_id']
        if 'quantity' in data:
            self.quantity = data['quantity']
        self.updated_at = datetime.utcnow()