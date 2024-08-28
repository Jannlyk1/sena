from app import db
from sqlalchemy.orm import relationship

class  Ventas (db.Model):
    __tablename__ = 'venta'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    id_clientes = db.Column(db.Integer, db.ForeignKey('cliente.id'))
