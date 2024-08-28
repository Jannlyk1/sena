from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes import clientes_routes, compras_routes, detallecompras_routes, detalleventas_routes,materiales_routes,muebles_routes,proveedores_routes,ventas_routes
    app.register_blueprint(clientes_routes.bp)
    app.register_blueprint(compras_routes.bp)
    app.register_blueprint(detallecompras_routes.bp)
    app.register_blueprint(detalleventas_routes.bp)
    app.register_blueprint(materiales_routes.bp)
    app.register_blueprint(muebles_routes.bp)
    app.register_blueprint(proveedores_routes.bp)
    app.register_blueprint(ventas_routes.bp)
    


    return app

