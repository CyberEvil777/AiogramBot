from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from db import Database
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from dotenv import load_dotenv
import os
from os.path import join, dirname


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)  # возвращен серкетный токен


# webhook settings
WEBHOOK_HOST = "https://abe54dc7eee8.ngrok.io"
WEBHOOK_PATH = ""
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 5000
token = get_from_env("TELEGRAM_BOT_TOKEN")

bot = Bot(token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
db = Database('database.db')
