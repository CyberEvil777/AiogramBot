import logging
import markups as nav
from aiogram import types
from aiogram.utils.executor import start_webhook
from core.constansts import ALL_COMMANDS
from core.config import (
    dp,
    bot,
    WEBHOOK_PATH,
    WEBAPP_HOST,
    WEBAPP_PORT,
    WEBHOOK_URL,
)
from user_behavior.subscribe_behavior import BehaviorSubscribe
from user_behavior.profile_behavior import ProfileBehavior
from user_behavior.information_behavior import InformationBehavior



logging.basicConfig(level=logging.INFO)


'''
@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)
'''


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Добро пожаловать",
        reply_markup=nav.get_sub_btn(),
    )


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        print(message)
        behavior_subscribe = BehaviorSubscribe(message.from_user.id)
        profile = ProfileBehavior()
        information = InformationBehavior()

        if message.text == '❤ ПОДПИСКА':
            await behavior_subscribe.subscribe_function()
        else:
            await behavior_subscribe.register_subscribe(message.text)

        if message.text == '👥 ПРОФИЛЬ':
            await profile.profile_logic(message.from_user.id)
        elif message.text == '🤔 ИНФОРМАЦИЯ':
            await information.profile_information(message.from_user.id)
        elif message.text == '💔 ОТПИСКА':
            await bot.send_message(message.from_user.id, "Отписку еще не придумали")
        elif message.text == '💗💗💗 Кого любит бот':
            user_nickname = message["from"]["first_name"]
            await bot.send_message(message.from_user.id, f"Бот любит {user_nickname}")
        elif not message.text in ALL_COMMANDS:
            await bot.send_message(message.from_user.id, "Что?")

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )