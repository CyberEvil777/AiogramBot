from core.config import bot
from core.config import db


class Behavior:
    """Class admin behavior"""
    def __init__(self):
        self.db = db
        self.bot = bot


def check_admin_exists(function_behavior):
    """Декоратор, который проверяет админ ли наш пользователь."""
    def wrapper(self, user_id, text):
        if user_id == 482930388:
            return function_behavior(self, user_id, text)

    return wrapper
