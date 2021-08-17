from .behavior import Behavior
from markups import mainMenu


class BehaviorSubscribe(Behavior):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    async def __check_data(self, message_text):
        if len(message_text) > 15:
            await self.bot.send_message(self.user_id, "Никнейм не должен превышать 15 символов")
        elif '@' in message_text or '/' in message_text:
            await self.bot.send_message(message_text, "Вы ввели запрещеный символ")
        else:
            self.db.set_nickname(self.user_id, message_text)
            self.db.set_signup(message_text, "done")
            await self.bot.send_message(
                self.user_id,
                "Регистрация прошла успешно!",
                reply_markup=mainMenu
            )

    async def register_subscribe(self, message_text):
        if self.db.get_signup(self.user_id) == "setnickname":
            await self.__check_data(message_text)

    async def subscribe_function(self):
        if not self.db.user_exists(self.user_id):
            self.db.add_user(self.user_id)
            await self.bot.send_message(self.user_id, "Укажите ваш ник")
        else:
            await self.bot.send_message(self.user_id, "Вы уже зарегистрированы!", reply_markup=mainMenu)
