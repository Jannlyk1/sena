from app import db
from sqlalchemy.orm import relationship

class  Muebles (db.Model):
    __tablename__ = 'mueble'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.String(255), nullable=False)
