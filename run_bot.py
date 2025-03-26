# Подключение aiogram модулей
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Импорт роутеров
from Routers import routers

# Подключение модуля асинхронных функций
import asyncio

TOKEN = '8024510098:AAFnNRXsxDdaroWYcJo_DtolkDwrvLwogOY'

bot = Bot(token=TOKEN) # Подключение бота
dp = Dispatcher(storage=MemoryStorage()) # Подключение диспетчера
async def main(): # Функция запуска
    # Подключение роутеров
    for router in routers: 
        dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)  # Отключение обработки сообщений в не рабочее время бота
    await dp.start_polling(bot) # Инийциализация бота

# Запуск
if __name__ == '__main__':  
    print('Бот начал работу') 
    asyncio.run(main())

 
