import logging
import markups as nav
from aiogram import types
from aiogram.utils.executor import start_webhook
from aiogram.types.message import ContentType
from core.constansts import ALL_COMMANDS
from core.config import (
    dp,
    bot,
    WEBHOOK_PATH,
    WEBAPP_HOST,
    WEBAPP_PORT,
    WEBHOOK_URL,
)
from user_behavior.registration_behavior import BehaviorRegistration
from user_behavior.profile_behavior import ProfileBehavior
from user_behavior.information_behavior import InformationBehavior
from user_behavior.subscribe_behavior import BehaviorSubscribe
from admin_behavior.post_behavior import PostBehavior

FORMAT = '%(asctime)s - Уровень %(levelname)s в %(filename)s.%(funcName)s: %(message)s'
logging.basicConfig(filename='log.txt', filemode='a', level=logging.INFO, format=FORMAT)
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
        behavior_subscribe = BehaviorRegistration(message.from_user.id)
        profile = ProfileBehavior()
        information = InformationBehavior()
        subscribe = BehaviorSubscribe()

        post = PostBehavior()

        if message.text == '❤ РЕГИСТРАЦИЯ':
            await behavior_subscribe.subscribe_function(message.text)
        else:
            await behavior_subscribe.register_subscribe(message.text)

        if message.text == '👥 ПРОФИЛЬ':
            await profile.profile_logic(message.from_user.id)
        elif message.text == '🤔 ИНФОРМАЦИЯ':
            await information.profile_information(message.from_user.id)
        elif message.text == '❤ ПОДПИСКА':
            await subscribe.subscribe_function(message.from_user.id)
        elif message.text == '💔 ОТПИСКА':
            await subscribe.unsubscribe_function(message.from_user.id)
        elif message.text == '💗💗💗 Кого любит бот':
            user_nickname = message["from"]["first_name"]
            await bot.send_message(message.from_user.id, f"Бот любит {user_nickname}")
        elif message.text == '🐯 Получит Стикеры':
            await bot.send_message(message.from_user.id, f"Ссылка на стикеры https://t.me/addstickers/AnimalsDaysStudio")
   

        elif message.text == '/admin'and message.from_user.id == 482930388:
            await bot.send_message(
                message.from_user.id,
                "Добро пожаловать в Админ панель",
                reply_markup=nav.get_admin_menu(),
            )
        elif not(message.text in ALL_COMMANDS) and message.from_user.id == 482930388:
            await post.post_information(message.from_user.id, message.text)

        elif message.text == 'POST' and message.from_user.id == 482930388:
            await post.profile_information(message.from_user.id)

        # elif not message.text in ALL_COMMANDS:
        #     await bot.send_message(message.from_user.id, "Что?")


# @dp.callback_query_handler(text="paymonth")
# async def pay_month(call: types.CallbackQuery):
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     await bot.send_invoice(chat_id=call.from_user.id, title="Оплатить курсы за месяц", description="Тестовая оплата товара", payload="month_sub", provider_token=YOO_TOKEN, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 550000}])
#
#
# @dp.pre_checkout_query_handlers(func=lambda query: True)
# async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
#
#
# @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
# async def process_pay(message: types.Message):
#     if message.successful_payment.invoice_payload == "month_sub":
#         # Оплачиваем курсы за месяц
#         await bot.send_message(message.from_user.id, "Вы оплатили курс за месяц")


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