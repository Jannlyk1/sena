from flask import Blueprint, render_template, redirect, url_for, request
from app.models.detallecompras import Detallecompras
from app import db

bp = Blueprint('detallecompras', __name__)

@bp.route('/detallecompras')
def index():
    data = Detallecompras.query.all()
    return render_template('detallecompra/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        costo  = request.form['costo']
        
        detallecompras=Detallescompras (costo=costo)

        db.session.add(detallecompras)
        db.session.commit()

        return redirect(url_for('detallecompras.index'))
    return render_template('detallecompra/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car = Detallecompras.query.get_or_404(id)
    if request.method == 'POST':
        detallecompras.costo = request.form['costo']
        
        
        db.session.commit()
        return redirect(url_for('detallecompras.index'))
    
    return render_template('detallecompra/edit.html', detallecompras=detallecompras)

@bp.route('/delete/<int:id>')
def delete(id):
    detallecompras = Detallecompras.query.get_or_404(id)
    db.session.delete(detallecompras)
    db.session.commit()
    return redirect(url_for('detallecompras.index'))