from flask import Blueprint, render_template, redirect, url_for, request
from app.models.detalleventas import Detalleventas
from app import db

bp = Blueprint('detalleventas', __name__)

@bp.route('/index')
def index():
    data = Detalleventas.query.all()
    return render_template('detalleventa/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        precio  = request.form['precio']
        
        detalleventas=Detalleventas (precio=precio)

        db.session.add(detalleventas)
        db.session.commit()

        return redirect(url_for('detalleventas.index'))
    return render_template('detalleventa/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car = Detalleventas.query.get_or_404(id)
    if request.method == 'POST':
        detalleventas.costo = request.form['costo']
        
        
        db.session.commit()
        return redirect(url_for('detalleventas.index'))
    
    return render_template('detalleventa/edit.html', detalleventas=detalleventas)

@bp.route('/delete/<int:id>')
def delete(id):
    detalleventas = Detalleventas.query.get_or_404(id)
    db.session.delete(detalleventas)
    db.session.commit()
    return redirect(url_for('detalleventas.index'))