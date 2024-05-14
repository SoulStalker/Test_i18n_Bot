from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
from aiogram.utils.i18n import gettext as _

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message):
    username = html.quote(message.from_user.full_name)
    button = InlineKeyboardButton(
        text=_('Кнопка'),
        callback_data='button_pressed'
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(
        text=_('Привет, {username}! Нажми на кнопку').format(username=username),
        reply_markup=markup
    )


@user_router.callback_query(F.data == 'button_pressed')
async def button_pressed(call: CallbackQuery):
    await call.answer(text=_('Вы нажали на кнопку'))


@user_router.message(Command('help'))
async def process_help(message: Message):
    await message.answer(
        text=_('Это бот для демонстрации процесса интернационализации\n\n'
               'Доступные команды:\n\n'
               '/start - перезапуск бота'
               '/help - справка по работе бота')
    )
