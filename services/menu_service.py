from abc import ABC
from time import time

from injector import inject

from dtos.menu_dto import MenuDto
from dtos.menu_extra_dto import MenuExtraDto
from exceptions import ResourceNotFoundException
from models import User, Menu, MenuExtra
from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.user_repository import UserRepository
from services.base_service import BaseService


class MenuService(BaseService, ABC):
    @inject
    def __init__(self,
                 repository: MenuRepository,
                 menu_extra_repo: MenuExtraRepository,
                 user_repo: UserRepository):
        super().__init__(repository)
        self.menu_extra_repo = menu_extra_repo
        self.user_repo = user_repo

    def find_all(self, query=None):
        resources = self.repository.find_all(query)
        return list(map(lambda menu: MenuDto(
            id=menu.id,
            menu_category=menu.menu_category,
            name=menu.name,
            description=menu.description,
            price=menu.price,
            menu_extras=list(map(lambda extra: MenuExtraDto.from_orm(extra), menu.menu_extras)),
            created_at=menu.created_at
        ).dict(), resources))

    def store(self, data):
        user = self.user_repo.find(data['user_id'])
        menu_extras = data['menu_extras']

        menu: Menu = self.repository.store({
            'menu_category_id': data['menu_category_id'],
            'restaurant_id': user.restaurant.id,
            'name': data['name'],
            'description': data['description'],
            'price': data['price'],
        })

        stored_extras = []

        if menu_extras is not None and len(menu_extras) > 0:
            for extra in menu_extras:
                extra['menu_id'] = menu.id
                stored_extra = self.menu_extra_repo.store(extra)
                stored_extras.append(MenuExtraDto.from_orm(stored_extra))

        menu_dto: MenuDto = MenuDto(
            id=menu.id,
            menu_category=menu.menu_category,
            name=menu.name,
            description=menu.description,
            price=menu.price,
            menu_extras=stored_extras,
            created_at=menu.created_at
        )
        return menu_dto.dict()

    def update(self, id, data):
        user: User = self.user_repo.find(data['user_id'])
        menu: Menu = self.repository.find(id)
        if menu is None:
            raise ResourceNotFoundException(description='Item not found')

        if menu.restaurant.id != user.restaurant.id:
            # TODO: throw access denied to resource exception
            pass

        updated_menu: Menu = self.repository.update(id, {
            'menu_category_id': data['menu_category_id'],
            'name': data['name'],
            'description': data['description'],
            'price': data['price'],
        })

        self.menu_extra_repo.delete_by_menu_id(menu.id)

        stored_extras = []

        for extra in data['menu_extras']:
            extra['menu_id'] = updated_menu.id
            stored_extra = self.menu_extra_repo.store(extra)
            stored_extras.append(MenuExtraDto.from_orm(stored_extra))

        menu_dto: MenuDto = MenuDto(
            id=menu.id,
            menu_category=updated_menu.menu_category,
            name=updated_menu.name,
            description=updated_menu.description,
            price=updated_menu.price,
            menu_extras=stored_extras,
            created_at=updated_menu.created_at
        )
        return menu_dto.dict()

    def delete_menu(self, id, user_id):
        user: User = self.user_repo.find(user_id)

        menu: Menu = self.repository.find(id)
        if menu is None:
            raise ResourceNotFoundException(description='Item not found')

        if menu.restaurant.id != user.restaurant.id:
            # TODO: throw access denied to resource exception
            pass

        self.menu_extra_repo.delete_by_menu_id(menu.id)
        self.repository.delete(id)

        return True

    def get_dto(self):
        return MenuDto
