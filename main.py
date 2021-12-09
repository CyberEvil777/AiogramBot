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

tech_anal = {
    'RU_anal': """1) STOCK = LKOH
Tech sell indicators: to buy = 9 of 12;  to sell = 0 of 12
SMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of LKOH = 7373.0 ; 7439.0 ; 7232.0 ; 7200.0 ; 7471.5
Percentage +/- of LKOH = +0.9% ; -2.78% ; -0.44% ; +3.77%

2) STOCK = OGKB
Tech sell indicators: to buy = 9 of 12;  to sell = 1 of 12
SMA moving averages: to buy = 5 of 6;  to sell = 1 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of OGKB = 0.7564 ; 0.7547 ; 0.7483 ; 0.723 ; 0.7549
Percentage +/- of OGKB = -0.22% ; -0.85% ; -3.38% ; +4.41%

3) STOCK = ROSN
Tech sell indicators: to buy = 10 of 12;  to sell = 0 of 12
SMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of ROSN = 643.0 ; 643.7 ; 633.3 ; 634.5 ; 655.8
Percentage +/- of ROSN = +0.11% ; -1.62% ; +0.19% ; +3.36%

4) STOCK = MSRS
Tech sell indicators: to buy = 10 of 12;  to sell = 0 of 12
SMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of MSRS = 1.419 ; 1.464 ; 1.413 ; 1.426 ; 1.445
Percentage +/- of MSRS = +3.17% ; -3.48% ; +0.92% ; +1.33%

5) STOCK = DASB
Tech sell indicators: to buy = 9 of 12;  to sell = 1 of 12
SMA moving averages: to buy = 5 of 6;  to sell = 1 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of DASB = 0.3133 ; 0.3444 ; 0.3786 ; 0.3331 ; 0.328
Percentage +/- of DASB = +9.93% ; +9.93% ; -12.02% ; -1.53%

6) STOCK = MRKC
Tech sell indicators: to buy = 9 of 12;  to sell = 1 of 12
SMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of MRKC = 0.44 ; 0.449 ; 0.4322 ; 0.4326 ; 0.441
Percentage +/- of MRKC = +2.05% ; -3.74% ; +0.09% ; +1.94%

7) STOCK = IGST
Tech sell indicators: to buy = 11 of 12;  to sell = 0 of 12
SMA moving averages: to buy = 5 of 6;  to sell = 1 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of IGST = 2025.0 ; 2060.0 ; 1890.0 ; 1760.0 ; 1901.0
Percentage +/- of IGST = +1.73% ; -8.25% ; -6.88% ; +8.01%

8) STOCK = IGST_p
Tech sell indicators: to buy = 10 of 12;  to sell = 0 of 12
SMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of IGST_p = 1915.0 ; 2389.0 ; 2445.0 ; 2080.0 ; 2286.0
Percentage +/- of IGST_p = +24.75% ; +2.34% ; -14.93% ; +9.9%

9) STOCK = KMAZ
Tech sell indicators: to buy = 9 of 12;  to sell = 2 of 12
SMA moving averages: to buy = 5 of 6;  to sell = 1 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of KMAZ = 122.8 ; 121.0 ; 114.5 ; 121.6 ; 118.0
Percentage +/- of KMAZ = -1.47% ; -5.37% ; +6.2% ; -2.96%

10) STOCK = MFGS_p
Tech sell indicators: to buy = 11 of 12;  to sell = 0 of 12
SMA moving averages: to buy = 5 of 6;  to sell = 1 of 6
EMA moving averages: to buy = 6 of 6;  to sell = 0 of 6
SMA_20 = buy ; SMA_100 = buy ; EMA_20 = buy ; EMA_100 = buy
Prices Last Five days of MFGS_p = 318.0 ; 324.0 ; 322.5 ; 316.0 ; 319.5
Percentage +/- of MFGS_p = +1.89% ; -0.46% ; -2.02% ; +1.11%
==================================================
Prices Last Five days of USD/RUB = 70.8265 ; 71.1022 ; 70.3281 ; 69.7474 ; 69.6511
Percentage +/- of USD/RUB = +0.39% ; -1.09% ; -0.83% ; -0.14%

""",

'USA_anal': """Пока не про Анализировал""",
}

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
        elif message.text == '💳 Технический Анализ Ru':
            await bot.send_message(message.from_user.id, tech_anal.get('RU_anal'))
        elif message.text == '💳 Технический Анализ USA':
            await bot.send_message(message.from_user.id, tech_anal.get('USA_anal'))

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