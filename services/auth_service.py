from abc import ABC
from passlib.hash import bcrypt

from flask_jwt_extended import create_access_token
from injector import inject

from dtos.auth_dto import AuthDto
from dtos.role_dto import RoleDto
from exceptions import EmailExistException
from models import User, Role
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from requests.login_request import LoginRequest
from requests.register_request import RegisterRequest
from services.base_service import BaseService


class AuthService(BaseService, ABC):

    @inject
    def __init__(self, repository: UserRepository, role_repository: RoleRepository):
        super().__init__(repository=repository)
        self.role_repository = role_repository

    def register(self, request: RegisterRequest):
        data = request.dict()
        del data['password_confirmation']

        role: Role = self.role_repository.find_by_name('Customer')
        data['role_id'] = role.id

        data['password'] = bcrypt.hash(request.password.encode())
        user = self.repository.store(data)

        token = create_access_token(identity=user.id, expires_delta=False)
        return self.__get_auth(user, token)

    def login(self, request: LoginRequest):
        user = self.repository.find_by_email(request.email)
        if user is None:
            return None
        if not bcrypt.verify(request.password, user.password):
            return None
        token = create_access_token(identity=user.id, expires_delta=False)
        return self.__get_auth(user, token)

    def get_dto(self):
        return AuthDto

    def __get_auth(self, user: User, token: str):
        return AuthDto(
            id=user.id,
            name=user.name,
            email=user.email,
            access_token=token,
            role=RoleDto(id=user.role.id, name=user.role.name).dict()
        ).dict()
