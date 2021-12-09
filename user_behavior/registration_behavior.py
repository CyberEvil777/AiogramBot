from .behavior import Behavior
from markups import get_main_menu


class BehaviorRegistration(Behavior):
    """Class for Registration behavior"""
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    async def __check_data(self, message_text):
        """Function check valid data, which user wrote"""
        if len(message_text) > 15:
            await self.bot.send_message(self.user_id, "Никнейм не должен превышать 15 символов")
        elif '@' in message_text or '/' in message_text:
            await self.bot.send_message(message_text, "Вы ввели запрещеный символ")
        else:
            self.db.set_nickname(self.user_id, message_text)
            self.db.set_signup(self.user_id, "done")
            await self.bot.send_message(
                self.user_id,
                "Регистрация прошла успешно!",
                reply_markup=get_main_menu()
            )

    async def register_subscribe(self, message_text):
        """Function check user registration """
        if self.db.get_signup(self.user_id) == "setnickname":
            await self.__check_data(message_text)

    async def subscribe_function(self, message_text):
        """Function registers users, if user have not nickname in database"""
        if not self.db.user_exists(self.user_id):
            self.db.add_user(self.user_id)
            await self.bot.send_message(self.user_id, "Укажите ваш ник")
        else:
            await self.bot.send_message(self.user_id, "Вы уже зарегистрированы!", reply_markup=get_main_menu())
