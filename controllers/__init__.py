from controllers.auth_controller import auth_bp
from controllers.restaurant_controller import restaurant_bp
from controllers.restaurant_registration_controller import restaurant_registration_bp


def register_routes(app, version):
    app.register_blueprint(auth_bp, url_prefix=f'/api/{version}auth')
    app.register_blueprint(restaurant_registration_bp, url_prefix=f'/api/{version}/restaurant_registrations')
    app.register_blueprint(restaurant_bp, url_prefix=f'/api/{version}/restaurants')
