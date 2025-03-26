from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def about():
    buttons = [[InlineKeyboardButton(text="Подробнее", url='https://telegra.ph/Kak-ty-smozhesh-zarabotat-2000-za-den-03-24'),
            InlineKeyboardButton(text="Отзывы", url='https://t.me/cash_towwn')],
            [InlineKeyboardButton(text="Хочу заработать", callback_data='money')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

end_admin_dialog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать рассылку", callback_data="start")],
        [InlineKeyboardButton(text="Отменить", callback_data="clear")]
    ]
)
