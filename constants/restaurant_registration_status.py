from enum import Enum


class RestaurantRegistrationStatus(str, Enum):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'
