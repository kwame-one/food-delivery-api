import uuid

from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from passlib.hash import bcrypt


def seed_super_admin():
    role_repo = RoleRepository()
    super_admin_role = role_repo.find_by_name('Super Admin')
    admin = {
        'name': 'The Super Administrator',
        'email': 'super@admin.com',
        'password': bcrypt.hash('password'),
        'role_id': super_admin_role.id,
    }
    repo = UserRepository()
    exists = repo.find_by_email(admin['email'])
    if exists is None:
        repo.store(admin)
