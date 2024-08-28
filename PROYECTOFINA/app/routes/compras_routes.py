from flask import Blueprint, render_template, redirect, url_for, request
from app.models.compras import Compras
from app import db

bp = Blueprint('compras', __name__)

@bp.route('/compras')
def index():
    data = Compras.query.all()
    return render_template('compras/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha  = request.form['fecha']
        total = request.form['total']
        

        compras=Compras (fecha=fecha, total=total)

        db.session.add(compras)
        db.session.commit()

        return redirect(url_for('compras.index'))
    return render_template('compras/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car = Compras.query.get_or_404(id)
    if request.method == 'POST':
        compras.fecha = request.form['fecha']
        compras.total = request.form['total'] 
        
        db.session.commit()
        return redirect(url_for('compras.index'))
    
    return render_template('compras/edit.html', compras=compras)

@bp.route('/delete/<int:id>')
def delete(id):
    compras = Compras.query.get_or_404(id)
    db.session.delete(compras)
    db.session.commit()
    return redirect(url_for('compras.index'))
