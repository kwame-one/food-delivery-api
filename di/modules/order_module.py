from injector import Module, singleton, provider

from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.order_item_repository import OrderItemRepository
from repositories.order_repository import OrderRepository
from services.order_service import OrderService


class OrderModule(Module):

    @singleton
    @provider
    def provide_order_repository(self) -> OrderRepository:
        return OrderRepository()

    @singleton
    @provider
    def provide_order_item_repository(self) -> OrderItemRepository:
        return OrderItemRepository()

    @singleton
    @provider
    def provide_order_service(self,
                              repository: OrderRepository,
                              order_item_repo: OrderItemRepository,
                              menu_repo: MenuRepository,
                              menu_extra_repo: MenuExtraRepository) -> OrderService:
        return OrderService(
            repository=repository,
            order_item_repo=order_item_repo,
            menu_repo=menu_repo,
            menu_extra_repo=menu_extra_repo)