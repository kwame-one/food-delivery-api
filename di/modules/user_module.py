from injector import Module, singleton, provider

from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.auth_service import AuthService


class UserModule(Module):

    @singleton
    @provider
    def provide_user_repository(self) -> UserRepository:
        return UserRepository()

    @singleton
    @provider
    def provide_auth_service(self, user_repository: UserRepository, role_repository: RoleRepository) -> AuthService:
        return AuthService(repository=user_repository, role_repository=role_repository)
