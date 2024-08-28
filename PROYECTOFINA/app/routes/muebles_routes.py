from flask import Blueprint, render_template, redirect, url_for, request
from app.models.muebles import Muebles
from app import db

bp = Blueprint('muebles', __name__)

@bp.route('/muebles')
def index():
    data = Muebles.query.all()
    return render_template('muebles/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre  = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        muebles=Muebles (nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad)

        db.session.add(muebles)
        db.session.commit()

        return redirect(url_for('muebles.index'))
    return render_template('muebles/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car =   Muebles.query.get_or_404(id)
    if request.method == 'POST':
        muebles.nombre = request.form['nombre']
        muebles.tipo = request.form['tipo'] 
        muebles.costo = request.form['costo']
        muebles.cantidad = request.form['cantidad']
        db.session.commit()
        return redirect(url_for('muebles.index'))
    
    return render_template('muebles/edit.html', muebles=muebles)

@bp.route('/delete/<int:id>')
def delete(id):
    muebles = Muebles.query.get_or_404(id)
    db.session.delete(muebles)
    db.session.commit()
    return redirect(url_for('muebles.index'))
