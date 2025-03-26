from aiogram import types, Router, F
from FSM import admin_dialog
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType

from start_hendler import users_list
from keyboards import end_admin_dialog
import asyncio

router = Router()
text = ''
file_id = None
start_index = 0
end_index = 0
admin_message = None

@router.message(F.text == 'Ольга')
async def admin(message: types.Message, state: FSMContext):
    global start_index
    await state.set_state(admin_dialog.password)
    authorization = await message.answer('Авторизация админа...')
    await asyncio.sleep(2)
    await authorization.edit_text('Введите пароль')
    start_index = authorization.message_id

@router.message(admin_dialog.password)
async def start_search(message: types.Message, state: FSMContext):  
    password = message.text
    if password == 'Olga08':
        await message.answer('Авторизация прошла успешено')
        await asyncio.sleep(1.5)
        await message.answer('Введите текст сообщения для рассылки')
        await state.set_state(admin_dialog.text_message)

    else:
        await message.answer('Не верный пароль')
        await state.clear()

@router.callback_query(F.data == 'clear')
async def clear_admin_autorization(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer('Рассылка отмененена. Для новой рассылки нужно заного авторизироваться', show_alert=True)
    end_index = await callback.message.answer('Сообщение с рассылкой удалено')
    await asyncio.sleep(5)
    for counter_message in range(start_index-1, end_index.message_id+1):
        await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=counter_message)
        await asyncio.sleep(0.5)

@router.callback_query(F.data == 'start')
async def clear_admin_autorization(callback: types.CallbackQuery, state: FSMContext):
    callback.answer('Рассылка запущена')
    counter = 0
    chat_id = callback.message.chat.id
    for user in users_list:
        if user != chat_id:
            await callback.message.bot.send_photo(chat_id=user, caption=text, photo=file_id)
            counter += 1
    await state.clear()
    end_index = await callback.message.answer(f'Количество пользователи получиливших рассылку {counter}')
    for counter_message in range(start_index-1, end_index.message_id+1):
        await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=counter_message)
        await asyncio.sleep(0.5)


@router.message(admin_dialog.text_message,)
async def start_search(message: types.Message, state: FSMContext):  
    global text
    text = message.text
    await message.answer('Отошлите фото для сообщения. Вжано: Фото не должно быть пересланным, его надо отправить с телефона')
    await state.set_state(admin_dialog.image_message)

@router.message(admin_dialog.image_message, lambda msg: msg.content_type ==ContentType.PHOTO)
async def handle_photo(message: types.Message, state: FSMContext):
    global text, admin_message, file_id
    photo = message.photo[-1]  # Берём фото наибольшего размера
    file_id = photo.file_id  # Получаем file_id
    admin_message = await message.answer_photo(file_id, caption=text)
    await message.answer('Сообщение для рассылки готово', reply_markup=end_admin_dialog)

    


    
    
