from flask import Blueprint, render_template, redirect, url_for, request
from app.models.ventas import Ventas
from app import db

bp = Blueprint('ventas', __name__)

@bp.route('/ventas')
def index():
    data = Ventas.query.all()
    return render_template('venta/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre  = request.form['nombre']
        fecha = request.form['fecha']
        correo = request.form['correo']

        ventas=Ventas (nombre=nombre, fecha=fecha,  correo=correo)

        db.session.add(ventas)
        db.session.commit()

        return redirect(url_for('ventas.index'))
    return render_template('venta/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car =   Ventas.query.get_or_404(id)
    if request.method == 'POST':
        ventas.nombre = request.form['nombre']
        ventas.fecha = request.form['fecha'] 
        ventas.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('ventas.index'))
    
    return render_template('venta/edit.html', ventas=ventas)

@bp.route('/delete/<int:id>')
def delete(id):
    Ventas = Ventas.query.get_or_404(id)
    db.session.delete(ventas)
    db.session.commit()
    return redirect(url_for('ventas.index'))
