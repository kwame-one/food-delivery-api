from injector import Module, singleton, provider

from repositories.role_repository import RoleRepository


class RoleModule(Module):

    @singleton
    @provider
    def provide_role_repository(self) -> RoleRepository:
        return RoleRepository()
