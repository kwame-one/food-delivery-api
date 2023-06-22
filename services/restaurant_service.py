from abc import ABC

from injector import inject
from passlib.hash import bcrypt

from dtos.restaurant_dto import RestaurantDto
from exceptions import EmailExistException
from models import User, Restaurant, Role
from repositories.restaurant_repository import RestaurantRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.base_service import BaseService
from utils import generate_password


class RestaurantService(BaseService, ABC):
    @inject
    def __init__(self,
                 repository: RestaurantRepository,
                 user_repo: UserRepository,
                 role_repo: RoleRepository):
        super().__init__(repository)
        self.user_repo = user_repo
        self.role_repo = role_repo

    def store(self, data):
        user_name = data['user_name']
        user_email = data['user_email']

        del data['user_name']
        del data['user_email']

        user: User = self.user_repo.find_by_email(user_email)
        if user is not None:
            raise EmailExistException()

        role: Role = self.role_repo.find_by_name('Restaurant Admin')

        new_user: User = self.user_repo.store({
            'name': user_name,
            'email': user_email,
            'password': bcrypt.hash(generate_password()),
            'role_id': role.id
        })

        data['user_id'] = new_user.id
        restaurant: Restaurant = self.repository.store(data)

        return RestaurantDto.from_orm(restaurant).dict()

    def get_dto(self):
        return RestaurantDto
