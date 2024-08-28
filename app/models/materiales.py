from app import db
from sqlalchemy.orm import relationship

class  Materiales(db.Model):
    __tablename__ = 'material'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(255), nullable=False)
    costo = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.String(255), nullable=False)

