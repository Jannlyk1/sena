from flask import Blueprint, render_template, redirect, url_for, request
from app.models.proveedores import Proveedores
from app import db

bp = Blueprint('proveedores', __name__)

@bp.route('/proveedores')
def index():
    data = Proveedores.query.all()
    return render_template('proveedor/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre  = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']

        proveedores=Proveedores (nombre=nombre, direccion=direccion, telefono=telefono, correo=correo)

        db.session.add(proveedores)
        db.session.commit()

        return redirect(url_for('proveedores.index'))
    return render_template('proveedor/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car =   Proveedores.query.get_or_404(id)
    if request.method == 'POST':
        proveedores.nombre = request.form['nombre']
        proveedores.direccion = request.form['direccion'] 
        proveedores.telefono = request.form['telefono']
        proveedores.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('proveedores.index'))
    
    return render_template('proveedor/edit.html', proveedores=proveedores)

@bp.route('/delete/<int:id>')
def delete(id):
    proveedores = Proveedores.query.get_or_404(id)
    db.session.delete(Proveedores)
    db.session.commit()
    return redirect(url_for('proveedores.index'))
