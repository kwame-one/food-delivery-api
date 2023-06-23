from controllers.auth_controller import auth_bp
from controllers.menu_category_controller import menu_category_bp
from controllers.menu_controller import menu_bp
from controllers.order_controller import order_bp
from controllers.order_status_controller import order_status_bp
from controllers.restaurant_controller import restaurant_bp
from controllers.restaurant_registration_controller import restaurant_registration_bp


def register_routes(app, version):
    app.register_blueprint(auth_bp, url_prefix=f'/api/{version}/auth')
    app.register_blueprint(restaurant_registration_bp, url_prefix=f'/api/{version}/restaurant_registrations')
    app.register_blueprint(restaurant_bp, url_prefix=f'/api/{version}/restaurants')
    app.register_blueprint(menu_category_bp, url_prefix=f'/api/{version}/menu_categories')
    app.register_blueprint(menu_bp, url_prefix=f'/api/{version}/menus')
    app.register_blueprint(order_bp, url_prefix=f'/api/{version}/orders')
    app.register_blueprint(order_status_bp, url_prefix=f'/api/{version}/order_statuses')
