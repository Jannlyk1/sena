from flask import Blueprint, render_template, redirect, url_for, request
from app.models.clientes import Clientes
from app import db

bp = Blueprint('clientes', __name__)

@bp.route('/')
def home():
    return render_template('home/index.html')

@bp.route('/index')
def index():
    data = Clientes.query.all()
    return render_template('clientes/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre  = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']

        clientes=Clientes (nombre=nombre, direccion=direccion, telefono=telefono, correo=correo)

        db.session.add(clientes)
        db.session.commit()

        return redirect(url_for('clientes.index'))
    return render_template('clientes/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car = Clientes.query.get_or_404(id)
    if request.method == 'POST':
        clientes.nombre = request.form['nombre']
        clientes.direccion = request.form['direccion'] 
        clientes.telefono = request.form['telefono']
        clientes.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('clientes.index'))
    
    return render_template('clientes/edit.html', clientes=clientes)

@bp.route('/delete/<int:id>')
def delete(id):
    clientes = Clientes.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.index'))
