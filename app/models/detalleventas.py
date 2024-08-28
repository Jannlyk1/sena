from app import db
from sqlalchemy.orm import relationship

class  Detalleventas (db.Model):
    __tablename__ = 'detalle_venta'
    id = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.String(255), nullable=False)
    id_ventas = db.Column(db.Integer, db.ForeignKey('venta.id'))
    id_muebles = db.Column(db.Integer, db.ForeignKey('mueble.id'))
