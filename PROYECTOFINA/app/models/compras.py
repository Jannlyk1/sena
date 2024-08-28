
from app import db
from sqlalchemy.orm import relationship

class  Compras(db.Model):
    __tablename__ = 'compra'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(255), nullable=False)
    total = db.Column(db.String(255), nullable=False)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id'))

