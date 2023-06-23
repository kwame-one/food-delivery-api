import json
import uuid
from abc import ABC

from injector import inject

from configs.database import db_session
from models import Order, UserOrder, OrderItem, Menu
from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.order_item_repository import OrderItemRepository
from repositories.order_repository import OrderRepository
from repositories.order_status_repository import OrderStatusRepository
from repositories.user_repository import UserRepository
from services.base_service import BaseService
from utils import generate_order_number


class OrderService(BaseService, ABC):
    @inject
    def __init__(self,
                 repository: OrderRepository,
                 order_item_repo: OrderItemRepository,
                 menu_repo: MenuRepository,
                 menu_extra_repo: MenuExtraRepository,
                 order_status_repo: OrderStatusRepository,
                 user_repo: UserRepository):
        super().__init__(repository)
        self.order_item_repo = order_item_repo
        self.menu_repo = menu_repo
        self.menu_extra_repo = menu_extra_repo
        self.order_status_repo = order_status_repo
        self.user_repo = user_repo

    def find_orders(self, user_id, query=None):
        user = self.user_repo.find(user_id)
        role_name = user.role.name
        restaurant_id = user.restaurant.id
        orders = []
        if role_name == 'Super Admin':
            orders = self.repository.find_all(query)
        elif role_name == 'Restaurant Admin':
            orders = self.repository.find_by_restaurant_id(restaurant_id)
        else:
            orders = self.repository.find_by_user_id(user_id)
        return None

    def store(self, data):
        cart = data['cart_items']
        user_id = data['user_id']
        menu_ids = [item['menu_id'] for item in cart]
        menu_extra_ids = [extra for item in cart for extra in item['menu_extras']]

        menus = self.menu_repo.find_by_id_in(menu_ids)
        menu_map = {item.id: item for item in menus}

        menu_extras = self.menu_extra_repo.find_by_id_in(menu_extra_ids)
        menu_extras_map = {item.id: item for item in menu_extras}
        menu_extra_map_2 = {item['menu_id']: list(map(lambda e: menu_extras_map.get(e), item['menu_extras'])) for item
                            in cart}

        menu_total = sum(list(map(lambda e: menu_map.get(e['menu_id']).price * e['quantity'], cart)))
        extra_total = sum(list(map(lambda e: menu_extras_map.get(e).price, menu_extra_ids)))

        grouped_menus = self.__group_order_request_by_restaurant(cart, menu_map, menu_extra_map_2)
        order_status = self.order_status_repo.find_by_name('Pending')

        user_order = self.__create_user_order({'user_id': user_id, 'total': menu_total + extra_total})

        for restaurant_id, menu_lists in grouped_menus.items():
            total = self.__caculate_total(menu_lists)

            order = self.__create_order({
                'order_number': generate_order_number(),
                'user_id': user_id,
                'user_order_id': user_order.id,
                'restaurant_id': restaurant_id,
                'order_status_id': order_status.id,
                'total': total,
            })

            self.__create_order_items(order, menu_lists)

        db_session.commit()

        return {'message': 'order has been placed successfully'}

    def get_dto(self):
        pass

    def __caculate_total(self, menu_lists):
        total = 0
        for menu_list in menu_lists:
            (menu, quantity, extras) = menu_list
            total = total + (menu.price * quantity) + sum([x.price for x in extras])
        return total

    def __group_order_request_by_restaurant(self, cart, menu_map, menu_extra_map_2):
        grouped_carts_by_restaurant = {}
        for item in cart:
            menu_item = menu_map.get(item['menu_id'])
            restaurant_id = menu_item.restaurant.id

            data = (menu_item, item['quantity'], menu_extra_map_2.get(item['menu_id'], []))

            if restaurant_id in grouped_carts_by_restaurant:
                restaurant_menus = grouped_carts_by_restaurant.get(restaurant_id)
                restaurant_menus.append(data)
                grouped_carts_by_restaurant[restaurant_id] = restaurant_menus
            else:
                grouped_carts_by_restaurant[restaurant_id] = [data]

        return grouped_carts_by_restaurant

    def __create_user_order(self, data):
        data['id'] = str(uuid.uuid4())
        user_order = UserOrder(**data)
        db_session.add(user_order)
        return user_order

    def __create_order(self, data):
        data['id'] = str(uuid.uuid4())
        order = Order(**data)
        db_session.add(order)
        return order

    def __create_order_items(self, order: Order, menu_lists):
        for menu_item in menu_lists:
            (menu, quantity, extras) = menu_item
            print(extras)
            data = {
                'id': str(uuid.uuid4()),
                'order_id': order.id,
                'menu_id': menu.id,
                'quantity': quantity,
                'menu_price': menu.price,
                'menu_extras': json.dumps([{'id': extra.id, 'name': extra.name, 'price': extra.price} for extra in extras])
            }
            order_item = OrderItem(**data)
            db_session.add(order_item)
