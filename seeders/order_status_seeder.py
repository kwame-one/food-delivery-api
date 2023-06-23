import uuid

from repositories.order_status_repository import OrderStatusRepository
from repositories.role_repository import RoleRepository


def seed_order_statuses():
    statuses = [
        {
            'name': 'Pending'
        },
        {
            'name': 'Fulfilled'
        },
        {
            'name': 'Rejected'
        }
    ]
    repo = OrderStatusRepository()
    for status in statuses:
        exists = repo.find_by_name(status['name'])
        if exists is None:
            repo.store(status)


