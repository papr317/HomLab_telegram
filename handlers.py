"""
обработчик интерфейса
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from services import call_homelab_app

router = Router()

# Главное меню с кнопками-пультами
@router.message(F.text)
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Проверить статус хомлаба", callback_data="action_status")],
        [InlineKeyboardButton(text="Управление Docker", callback_data="action_docker")],
                [InlineKeyboardButton(text="Добавить торрент", callback_data="action_torrent")]

    ])
    await message.answer("**Панель управления Хомлабом:**\nВыберите действие:", reply_markup=keyboard, parse_mode="Markdown")

# Обработка нажатия на кнопку "Проверить статус"
@router.callback_query(F.data == "action_status")
async def btn_status(callback: CallbackQuery):
    result = call_homelab_app("status")
    await callback.message.answer(result)
    await callback.answer()
    

# Обработка нажатия на кнопку "Управление Docker"
@router.callback_query(F.data == "action_docker")
async def btn_docker(callback: CallbackQuery):
    result = call_homelab_app("docker")
    await callback.message.answer(result)
    await callback.answer()
    
    
# Обработка нажатия на кнопку "Добавить торрент"
@router.callback_query(F.data == "action_torrent")
async def btn_torrent(callback: CallbackQuery):
    # Вызываем сервис
    result = call_homelab_app("torrent")
    
    # Отвечаем пользователю и убираем "часики" загрузки с кнопки
    await callback.message.answer(result)
    await callback.answer()