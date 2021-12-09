from .behavior import Behavior
from .behavior import check_user_exists


class InformationBehavior(Behavior):
    """Class for information behavior"""

    def __init__(self):
        super().__init__()

    @check_user_exists
    async def profile_information(self, user_id):
        """Function get information about buttons"""
        await self.bot.send_message(user_id, "👥 ПРОФИЛЬ - информация о профиле\n"
                                             "❤ ПОДПИСКА - подписка на уведомления\n"
                                             "💔 ОТПИСКА - отписка от уведомлений")

