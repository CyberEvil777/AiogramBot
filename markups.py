from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# btnSub = KeyboardButton('❤ ПОДПИСКА')
#
# mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
# mainMenu.add(btnSub)


def get_main_menu():
    btn_profile = KeyboardButton('👥 ПРОФИЛЬ')
    btn_sub = KeyboardButton('❤ ПОДПИСКА')
    btn_un_sub = KeyboardButton('💔 ОТПИСКА')
    btn_inf = KeyboardButton('🤔 ИНФОРМАЦИЯ')
    btn_love = KeyboardButton('💗💗💗 Кого любит бот')
    btn_pay = KeyboardButton('💳 Оплата за месяц')
    btn_stick = KeyboardButton('🐯 Получит Стикеры')
    btn_ru_anal = KeyboardButton('💳 Технический Анализ Ru')
    btn_usa_anal = KeyboardButton('💳 Технический Анализ USA')

    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.add(btn_profile, btn_sub, btn_un_sub, btn_inf, btn_love, btn_stick, btn_ru_anal, btn_usa_anal)

    return main_menu


def get_sub_btn():
    btn_sub = KeyboardButton('❤ РЕГИСТРАЦИЯ')

    sub_scribe = ReplyKeyboardMarkup(resize_keyboard=True)
    sub_scribe.add(btn_sub)

    return sub_scribe

def get_admin_menu():
    btn_profile = KeyboardButton('👥 ПРОФИЛЬ')
    btn_inf = KeyboardButton('🤔 ИНФОРМАЦИЯ')
    btn_post = KeyboardButton('POST')


    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.add(btn_profile, btn_inf, btn_post)

    return main_menu


# def get_pay_course():
# pay_inline_markup = InlineKeyboardMarkup(row_width=1)
# btn_pay = InlineKeyboardButton(text='Оплата курсов по python за месяц', callback_data="paymonth")
# btn_inline = pay_inline_markup.insert(btn_pay)

    # return btn_inline