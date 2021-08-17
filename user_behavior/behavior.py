from core.config import bot
from core.config import db


class Behavior:
    def __init__(self):
        self.db = db
        self.bot = bot


def check_user_exists(function_behavior):
    """Декоратор, который проверяет существует ли пользователь в бд."""
    def wrapper(self, user_id):
        if db.user_exists(user_id):
            return function_behavior(self, user_id)

    return wrapper
