from .behavior import Behavior
from .behavior import check_user_exists


class BehaviorSubscribe(Behavior):
    """Class for Subscribe behavior"""
    def __init__(self):
        super().__init__()

    @check_user_exists
    async def subscribe_function(self, user_id):
        """Function subscribe user"""
        self.db.set_sub(user_id, time_sub=1)
        await self.bot.send_message(user_id, "Вы подписаны на уведомления")

    @check_user_exists
    async def unsubscribe_function(self, user_id):
        """Function unsubscribe user"""
        self.db.set_sub(user_id, time_sub=0)
        await self.bot.send_message(user_id, "Вы отписаны от уведомлений")