from .behavior import Behavior
from .behavior import check_user_exists


class ProfileBehavior(Behavior):
    """Class for information behavior"""

    def __init__(self):
        super().__init__()

    @check_user_exists
    async def profile_logic(self, user_id, time_sub=1):
        """Function get Nickname user"""
        user_nickname = "Ваш ник: " + self.db.get_nickname(user_id)
        await self.bot.send_message(user_id, user_nickname)



