from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
from fluentogram import TranslatorRunner

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message, i18n: TranslatorRunner):
    username = html.quote(message.from_user.full_name)
    button = InlineKeyboardButton(
        text=i18n.button.button(),
        callback_data='button_pressed'
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(
        text=i18n.hello.user(username=username),
        reply_markup=markup
    )


@user_router.callback_query(F.data == 'button_pressed')
async def button_pressed(call: CallbackQuery, i18n: TranslatorRunner):
    await call.answer(text=i18n.button.pressed())

#
# @user_router.message(Command('help'))
# async def process_help(message: Message):
#     await message.answer(
#         text=_('Это бот для демонстрации процесса интернационализации\n\n'
#                'Доступные команды:\n\n'
#                '/start - перезапуск бота'
#                '/help - справка по работе бота')
#     )
