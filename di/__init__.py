from flask_injector import FlaskInjector

from .modules.menu_category_module import MenuCategoryModule
from .modules.menu_module import MenuModule
from .modules.restaurant_module import RestaurantModule
from .modules.restaurant_registration_module import RestaurantRegistrationModule
from .modules.role_module import RoleModule
from .modules.user_module import UserModule


def init_container(app):
    FlaskInjector(app=app, modules=[
        UserModule,
        RoleModule,
        RestaurantModule,
        RestaurantRegistrationModule,
        MenuCategoryModule,
        MenuModule,
    ])
