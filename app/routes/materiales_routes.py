from flask import Blueprint, render_template, redirect, url_for, request
from app.models.materiales import Materiales
from app import db

bp = Blueprint('materiales', __name__)

@bp.route('/materiales')
def index():
    data = Materiales.query.all()
    return render_template('materiales/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre  = request.form['nombre']
        tipo = request.form['tipo']
        costo = request.form['costo']
        cantidad = request.form['cantidad']

        materiales=Materiales (nombre=nombre, tipo=tipo, costo=costo, cantidad=cantidad)

        db.session.add(materiales)
        db.session.commit()

        return redirect(url_for('materiales.index'))
    return render_template('materiales/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car =   Materiales.query.get_or_404(id)
    if request.method == 'POST':
        materiales.nombre = request.form['nombre']
        materiales.tipo = request.form['tipo'] 
        materiales.costo = request.form['costo']
        materiales.cantidad = request.form['cantidad']
        db.session.commit()
        return redirect(url_for('materiales.index'))
    
    return render_template('materiales/edit.html', materiales=materiales)

@bp.route('/delete/<int:id>')
def delete(id):
    materiales = Materiales.query.get_or_404(id)
    db.session.delete(materiales)
    db.session.commit()
    return redirect(url_for('materiales.index'))
