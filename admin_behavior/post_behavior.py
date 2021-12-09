from .behavior import Behavior
from .behavior import check_admin_exists


class PostBehavior(Behavior):
    """Class Post behavior"""

    def __init__(self):
        super().__init__()

    @check_admin_exists
    async def post_information(self, user_id, text):
        """Function which post infomation from bot
           Each user will see information, which you posted
        """
        users_data = self.db.get_all_sub()
        for chat_id in users_data:
            await self.bot.send_message(chat_id[0], text)

    async def profile_information(self, user_id):

        await self.bot.send_message(user_id, "POST - Чтобы сделать Пост\n"
                                            "для всех пользователей, необходимо\n"
                                            "написать текст, который не связан\n"
                                            " с командами пользователя или админа")

