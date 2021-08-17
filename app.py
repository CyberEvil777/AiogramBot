import logging
import markups as nav
from db import Database

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


API_TOKEN = "1946256696:AAEitJpw_fZMvSSukOyVCAZ3E_Z2GQGHEsE"

# webhook settings
WEBHOOK_HOST = "https://4d1e3b92aa95.ngrok.io"
WEBHOOK_PATH = ""
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 5000

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)


'''
@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)
'''
class mainBot():
    dp = Dispatcher(bot)
    def __init__ (self, API_TOKEN):
        self.bot = Bot(token=API_TOKEN)
        self.dp = Dispatcher(bot)
        self.dp.middleware.setup(LoggingMiddleware())
        self.db = Database('database.db')



    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await bot.send_message(message.from_user.id, "Добро пожаловать", reply_markup=nav.mainMenu)


    @dp.message_handler()
    async def bot_message(message: types.Message):
        if message.chat.type == 'private':
            print(message)
            if message.text == '👥 ПРОФИЛЬ':
                user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)
                await bot.send_message(message.from_user.id, user_nickname)
            elif message.text == '❤ ПОДПИСКА':
                if (not db.user_exists(message.from_user.id)):
                    db.add_user(message.from_user.id)
                    await bot.send_message(message.from_user.id, "Укажите ваш ник")
                else:
                    await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup=nav.mainMenu)
            else:
                if db.get_signup(message.from_user.id) == "setnickname":
                    if(len(message.text) > 15):
                        await bot.send_message(message.from_user.id, "Никнейм не должен превышать 15 символов")
                    elif '@' in message.text or '/' in message.text:
                        await bot.send_message(message.from_user.id, "Вы ввели запрещеный символ")
                    else:
                        db.set_nickname(message.from_user.id, message.text)
                        db.set_signup(message.from_user.id, "done")
                        await bot.send_message(message.from_user.id, "Регистрация прошла успешно!", reply_markup=nav.mainMenu)
                else:
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