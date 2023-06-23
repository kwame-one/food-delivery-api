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
        exists = repo.find_by_name(role['name'])
        if exists is None:
            repo.store(role)


