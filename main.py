import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

bot = Bot(token="7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg")
dp = Dispatcher()
router = Router()


class Anketa(StatesGroup):
     name = State()
     age = State()
     gender = State()


@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
          InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]])
    await msg.answer('Введите Ваше имя', reply_markup=markup)
  
@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext): 
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')
 
@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext): 
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text'Назад', callback_data='back_anketa'),
        InlineKeyboardButton(text'Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите Ваш возраст', reply_markup=markup)
   

async def main():
        await dp.start_polling(bot)

dp.include_routers(router)

if name == 'main':
    asyncio.run(main())