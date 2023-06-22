from abc import ABC

from injector import inject

from constants.restaurant_registration_status import RestaurantRegistrationStatus
from dtos.restaurant_registration_dto import RestaurantRegistrationDto
from exceptions import ResourceNotFoundException, EmailExistException
from models import Role, User
from models.restaurant_registration import RestaurantRegistration
from repositories.restaurant_registration_repository import RestaurantRegistrationRepository
from repositories.restaurant_repository import RestaurantRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.base_service import BaseService
from passlib.hash import bcrypt


class RestaurantRegistrationService(BaseService, ABC):
    @inject
    def __init__(self, repository: RestaurantRegistrationRepository,
                 user_repo: UserRepository,
                 restaurant_repo: RestaurantRepository,
                 role_repo: RoleRepository):

        super().__init__(repository=repository)
        self.user_repo = user_repo
        self.restaurant_repo = restaurant_repo
        self.role_repo = role_repo

    def store(self, data):
        data['status'] = RestaurantRegistrationStatus.PENDING.value
        return super().store(data)

    def update(self, id, data):
        resource: RestaurantRegistration = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')

        if resource.status != RestaurantRegistrationStatus.PENDING.value:
            return self.get_dto().from_orm(resource).dict()

        user: User = self.user_repo.find_by_email(resource.user_email)

        if user is not None:
            # TODO send email to user about informing them their email has also been recorded in the system
            raise EmailExistException()

        status = RestaurantRegistrationStatus.APPROVED.value if data['approve'] \
            else RestaurantRegistrationStatus.REJECTED.value

        new_data = {'status': status}
        dto = self.get_dto().from_orm(self.repository.update(id, new_data)).dict()

        if data['approve']:
            self.__create_record(resource)

        return dto

    def get_dto(self):
        return RestaurantRegistrationDto

    def __create_record(self, resource: RestaurantRegistration):
        """
            create user record and restaurant record
        """
        role: Role = self.role_repo.find_by_name('Restaurant Admin')

        user_data = {
            'name': resource.user_name,
            'email': resource.user_email,
            'password': bcrypt.hash(self.__generate_password()),
            'role_id': role.id
        }
        new_user: User = self.user_repo.store(user_data)

        restaurant_data = {
            'user_id': new_user.id,
            'name': resource.restaurant_name,
            'email': resource.restaurant_email,
            'address': resource.restaurant_address,
            'phone': resource.restaurant_phone,
        }
        self.restaurant_repo.store(restaurant_data)

    def __generate_password(self):
        return 'password'
