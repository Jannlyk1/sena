from app import db
from sqlalchemy.orm import relationship

class Detallecompras (db.Model):
   __tablename__ = 'detalle_compra'
   id = db.Column(db.Integer, primary_key=True)
   costos = db.Column(db.String(255), nullable=False)
   id_compra = db.Column(db.Integer, db.ForeignKey('compra.id'))
   id_materiales = db.Column(db.Integer, db.ForeignKey('material.id'))

