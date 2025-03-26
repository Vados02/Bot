from aiogram.fsm.state import State, StatesGroup

class admin_dialog(StatesGroup):
    password = State()
    text_message = State()
    image_message = State()