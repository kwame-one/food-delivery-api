from abc import abstractmethod

from exceptions.not_found_exception import ResourceNotFoundException


class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def find_all(self, query=None):
        resources = self.repository.find_all(query)
        return list(map(lambda x: self.get_dto().from_orm(x).dict(), resources))

    def find(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')
        return self.get_dto().from_orm(resource).dict()

    def update(self, id, data):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')
        return self.get_dto().from_orm(self.repository.update(id, data)).dict()

    def store(self, data):
        resource = self.repository.store(data)
        return self.get_dto().from_orm(resource).dict()

    def delete(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')
        self.repository.delete(id)
        return True

    @abstractmethod
    def get_dto(self):
        pass
