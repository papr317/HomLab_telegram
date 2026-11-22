"""
обработчик интерфейса
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from services import call_homelab_app

router = Router()

MAIN_MENU_TEXT = "**Панель управления homlab:**\nВыберите действие:"


def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Проверить статус хомлаба 📊", callback_data="action_status")],
        [InlineKeyboardButton(text="Управление Docker 🐳", callback_data="action_docker")],
        [InlineKeyboardButton(text="Добавить торрент 🧲", callback_data="action_torrent")]
    ])


def get_back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="вернуться к меню ⬅️", callback_data="back")]
    ])


# Главное меню с кнопками-пультами
@router.message(F.text)
async def cmd_start(message: Message, admin_id: int):
    if message.from_user.id != admin_id:
        return

    await message.answer(MAIN_MENU_TEXT, reply_markup=get_main_keyboard(), parse_mode="Markdown")


# Обработка нажатия на кнопку "Проверить статус"
@router.callback_query(F.data == "action_status")
async def btn_status(callback: CallbackQuery, admin_id: int):
    if callback.from_user.id != admin_id:
        await callback.answer("кто нажалал тот гей", show_alert=True)
        return

    result = call_homelab_app("status")
    await callback.message.edit_text(result, reply_markup=get_back_keyboard())
    await callback.answer()


# Обработка нажатия на кнопку "Управление Docker"
@router.callback_query(F.data == "action_docker")
async def btn_docker(callback: CallbackQuery, admin_id: int):
    if callback.from_user.id != admin_id:
        await callback.answer("кто нажалал тот гей", show_alert=True)
        return

    result = call_homelab_app("docker")
    await callback.message.edit_text(result, reply_markup=get_back_keyboard())
    await callback.answer()


# Обработка нажатия на кнопку "Добавить торрент"
@router.callback_query(F.data == "action_torrent")
async def btn_torrent(callback: CallbackQuery, admin_id: int):
    if callback.from_user.id != admin_id:
        await callback.answer("кто нажалал тот гей", show_alert=True)
        return

    result = call_homelab_app("torrent")
    await callback.message.edit_text(result, reply_markup=get_back_keyboard())
    await callback.answer()


# Кнопка "вернуться к меню"
@router.callback_query(F.data == "back")
async def btn_back(callback: CallbackQuery, admin_id: int):
    if callback.from_user.id != admin_id:
        await callback.answer("кто нажалал тот гей", show_alert=True)
        return

    await callback.message.edit_text(MAIN_MENU_TEXT, reply_markup=get_main_keyboard(), parse_mode="Markdown")
    await callback.answer()