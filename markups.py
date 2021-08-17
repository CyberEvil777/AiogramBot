from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnSub = KeyboardButton('❤ ПОДПИСКА')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnSub)


def get_main_menu():
    btn_profile = KeyboardButton('👥 ПРОФИЛЬ')
    btn_sub = KeyboardButton('❤ ПОДПИСКА')
    btn_un_sub = KeyboardButton('💔 ОТПИСКА')
    btn_inf = KeyboardButton('🤔 ИНФОРМАЦИЯ')
    btn_love = KeyboardButton('💗💗💗 Кого любит бот')

    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.add(btn_profile, btn_sub, btn_un_sub, btn_inf, btn_love)

    return main_menu


def get_sub_btn():
    btn_sub = KeyboardButton('❤ ПОДПИСКА')

    sub_scribe = ReplyKeyboardMarkup(resize_keyboard=True)
    sub_scribe.add(btn_sub)

    return sub_scribe
