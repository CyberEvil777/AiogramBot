from .behavior import Behavior
from .behavior import check_user_exists


class InformationBehavior(Behavior):

    def __init__(self):
        super().__init__()

    @check_user_exists
    async def profile_information(self, user_id):
        await self.bot.send_message(user_id, "👥 ПРОФИЛЬ - информация о профиле\n"
                                             "❤ ПОДПИСКА - подписка на уведомления\n"
                                             "💔 ОТПИСКА - отписка от уведомлений")

