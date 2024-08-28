from app import db
from sqlalchemy.orm import relationship

class  Proveedores (db.Model):
   __tablename__ = 'proveedor'
   id = db.Column(db.Integer, primary_key=True)
   nombre = db.Column(db.String(255), nullable=False)
   direccion = db.Column(db.String(255), nullable=False)
   telefono = db.Column(db.String(255), nullable=False)
   correo = db.Column(db.String(255), nullable=False)
