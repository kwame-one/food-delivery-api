from abc import ABC

from injector import inject

from dtos.menu_category_dto import MenuCategoryDto
from repositories.menu_category_repository import MenuCategoryRepository
from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.order_item_repository import OrderItemRepository
from repositories.order_repository import OrderRepository
from services.base_service import BaseService


class OrderService(BaseService, ABC):
    @inject
    def __init__(self,
                 repository: OrderRepository,
                 order_item_repo: OrderItemRepository,
                 menu_repo: MenuRepository,
                 menu_extra_repo: MenuExtraRepository):
        super().__init__(repository)
        self.order_item_repo = order_item_repo
        self.menu_repo = menu_repo
        self.menu_extra_repo = menu_extra_repo

    def store(self, data):
        cart = data['cart_items']
        user_id = data['user_id']
        menu_ids = [item['menu_id'] for item in cart]
        menu_extra_ids = [extra for item in cart for extra in item['menu_extras']]

        menus = self.menu_repo.find_by_id_in(menu_ids)
        menu_map = {item.id: item for item in menus}

        menu_extras = self.menu_extra_repo.find_by_id_in(menu_extra_ids)
        menu_extras_map = {item.id: item for item in menu_extras}

        menu_total = sum(list(map(lambda e: menu_map.get(e['menu_id']).price * e['quantity'], cart)))
        extra_total = sum(list(map(lambda e: menu_extras_map.get(e), menu_extra_ids)))

        print(menu_total)
        print(extra_total)

        grouped_menus = self.__group_order_request_by_restaurant(cart, menu_map)
        print(grouped_menus)

        return None

    def get_dto(self):
        pass

    def __group_order_request_by_restaurant(self, cart, menu_map):
        grouped_carts_by_restaurant = {}
        for item in cart:
            menu_item = menu_map.get(item['menu_id'])
            restaurant_id = menu_item.restaurant.id

            if restaurant_id in grouped_carts_by_restaurant:
                restaurant_menus = grouped_carts_by_restaurant.get(restaurant_id)
                restaurant_menus.append((menu_item, item['quantity']))
                grouped_carts_by_restaurant[restaurant_id] = restaurant_menus
            else:
                grouped_carts_by_restaurant[restaurant_id] = [(menu_item, item['quantity'])]

        return grouped_carts_by_restaurant
