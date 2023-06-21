import uuid

from repositories.role_repository import RoleRepository


def seed_roles():
    roles = [
        {
            'id': str(uuid.uuid4()),
            'name': 'Super Admin'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Restaurant Admin'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Customer'
        }
    ]
    repo = RoleRepository()
    for role in roles:
        repo.store(role)

