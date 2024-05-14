from aiogram import F, Router, html
from aiogram.filters import  CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message):
    username = html.quote(message.from_user.full_name)
    button = InlineKeyboardButton(
        text='Кнопка',
        callback_data='button_pressed'
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(
        text='Привет, {username}! Нажми на кнопку'.format(username=username),
        reply_markup=markup
    )


@user_router.callback_query(F.data == 'button_pressed')
async def button_pressed(call: CallbackQuery):
    await call.answer(text='Вы нажали на кнопку')