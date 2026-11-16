# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router
import os
from dotenv import load_dotenv

# Вставляем ваши данные напрямую (или можно вынести в .env, как обсуждали)
load_dotenv()

BOT_TOKEN = os.getenv("Bot_TOKEN")
ADMIN_ID = int(os.getenv("MY_ID_TOKEN", 0))

async def main():
    # Инициализируем бота
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # чтобы хендлеры знали, кто главный администратор
    dp["admin_id"] = ADMIN_ID
    
    # Подключаем роутер с кнопками и хендлерами из handlers.py
    dp.include_router(router)
    
    print("Бот-панель управления успешно запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())