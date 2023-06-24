from time import time


def generate_password():
    return 'password'


def generate_order_number():
    return time()


def get_offset(page=None, limit=20):
    p = int('0' if page == '' else str(page))
    if p <= 1:
        return 0
    return (p - 1) * limit
