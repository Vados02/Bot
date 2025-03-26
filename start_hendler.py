# Ипорт модулей aiogram
from aiogram.filters import Command
from aiogram import types, Router, F
from FSM import admin_dialog
from aiogram.fsm.context import FSMContext

import asyncio

from keyboards import about

router = Router() # Создание роутера
users_list = set()
counter_u = 0
@router.message(Command('start'))
async def post(message: types.Message):
    global users_list, counter_u
    counter_u += 1
    print(counter_u)
    chat_id= message.chat.id
    if chat_id not in users_list:
        users_list.add(chat_id)

    await message.delete()
    text = "Привет!"
    sent_message = await message.answer("</>")
    full_message = ""
    delay = 0.2 # Уменьшаем задержку для более плавного чтения
    for letter in text:
        full_message += letter
        await sent_message.edit_text(full_message + " \u200B")
        await asyncio.sleep(delay)
    await asyncio.sleep(2)
    start_list_1 = ['Ты же пришел сюда, чтобы подзаработать? Верно?', 'Тогда не буду лить лишнюю воду.', 'Кто я такой сейчас не особо важно, познакомиться можем лично в чате.', 'Куда интереснее то, как ты можешь сделать свой кошелек тяжелее.', 'Сейчас внизу появиться панель \U0001f447']

    for i in start_list_1:
        await sent_message.edit_text(i)
        await asyncio.sleep(4)
    await message.answer_photo(photo='https://disk.yandex.ru/i/nghJLptGeLprcQ', caption=f'Жми на кнопку ниже', reply_markup=about())
    await message.bot.delete_message(chat_id = message.chat.id, message_id=sent_message.message_id)
    await asyncio.sleep(3)
    await message.answer('Тут ты найдешь все что тебе нужно. Для начала нажми на кнопку Подробнее.')

@router.callback_query(F.data == "money")
async def start_search(callback: types.CallbackQuery):
    await callback.answer('Удачного зароботка!')
    await callback.message.answer('Личка открыта всегда, днем отвечу в течении часа - @alexei_abdeev')