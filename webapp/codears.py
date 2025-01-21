import asyncio
import random


from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter

bot = Bot(token="7763885193:AAEvUvBH0jm7zY02BOHGrUkLdoUK6FMX6fo")
dp = Dispatcher()

class OrderFood(StatesGroup):
    choosing_food_name = State()
    choosing_food_size = State()


@dp.message(CommandStart())
async def osnova_otvetov(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Каталог Мессье",
        callback_data="otk_katalog")
    )
    builder.add(types.InlineKeyboardButton(
         text="Созвездия",
         callback_data="star_katalog")
    )



    await message.answer(
        'Привет, Астроном! \nЧтобы начать своё обучение, выберите режим квиза.'
    '\n\n1.  Если вы выберете названия Messier, то вам надо будет просто отгадать номер из каталога Мессье. В ответ вводите только номер.'
    '\nА если вы выберете созвездия Messier, то вам надо будет угадать созвездие, в котором находится объект. '
        '\nТакже у вас будет ссылка на полный каталог, если возникнут проблемы. \n '
        '\n2.  Вы выбрали Созвездия:'
        '\nЕсли вы выберете Название созвездий, то вам надо будет отгадать название созвездия, изображенного на картинке.'
        '\nА если вы выберете Яркие звезды созвездий, то вам надо будет отгадать самую яркую звезду в созвездии, которое находится на картинке.'
        '\nЕсли у вас возникнут проблемы в квизе, можете воспользоваться программой Stellarium.'
        '\nПосле того, как вы выбрали режим, нажимайте /get_photo для получения фотографии обьекта.'
        'Все названия вводите с заглавной буквы.  Удачи!',
        reply_markup=builder.as_markup(),
    )

@dp.callback_query(F.data == "otk_katalog")
async def otk_katal(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Каталог Мессье", url="https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%9C%D0%B5%D1%81%D1%81%D1%8C%D0%B5")
    )
    builder.add(types.InlineKeyboardButton(
        text="Названия Messier",
        callback_data="vybor_quiz_mesie1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Созвездия Messier",
        callback_data="vybor_quiz_mesie2")
    )
    await callback.message.answer(
         text='Выбери функцию',
         reply_markup=builder.as_markup(),
    )
    await callback.answer()
@dp.callback_query(F.data == "star_katalog")
async def sta_katal(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
         text="Названия созвездий",
         callback_data="vybor_quiz_const1")
    )
    builder.add(types.InlineKeyboardButton(
         text="Яркие звезды созвездий",
         callback_data="vybor_quiz_const2")
    )

    await callback.message.answer(
        text = 'Выбери функцию',
        reply_markup=builder.as_markup(),
    )
    await callback.answer()


@dp.callback_query(F.data == "vybor_quiz_mesie1")
async def vybor_sl1(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(OrderFood.choosing_food_name)
    await state.update_data(sloshnost = 1)
    await callback.answer(text='Вы выбрали названия messier')

@dp.callback_query(F.data == "vybor_quiz_mesie2")
async def vybor_sl2(callback: types.CallbackQuery,state: FSMContext):
    await state.set_state(OrderFood.choosing_food_name)
    await state.update_data(sloshnost = 2)
    await callback.answer(text='Вы выбрали созвездия messier')

@dp.callback_query(F.data == "vybor_quiz_const1")
async def vybor_sl3(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(OrderFood.choosing_food_name)
    await state.update_data(sloshnost = 3)
    await callback.answer(text='Вы выбрали названия созвездий')

@dp.callback_query(F.data == "vybor_quiz_const2")
async def vybor_sl4(callback: types.CallbackQuery,state: FSMContext):
    await state.set_state(OrderFood.choosing_food_name)
    await state.update_data(sloshnost = 4)
    await callback.answer(text='Вы выбрали яркие звезды созвездий')

@dp.message(F.photo)
async def get_photoid(message: Message):
    await message.answer(message.photo[-1].file_id)

@dp.message(Command("get_photo"))
async def get_photo(message: Message, state: FSMContext):
    user_data = await state.get_data()

    answer_s1 = random.choice(list(d))
    if user_data["sloshnost"] == 1:
        answer_s1 = random.choice(list(d))
        await state.update_data(answer_s = answer_s1)
        await state.update_data(answer_z = d[answer_s1])
    if user_data["sloshnost"] == 2:
        answer_s1 = random.choice(list(s))
        await state.update_data(answer_s = answer_s1)
        await state.update_data(answer_z = s[answer_s1])
    if user_data["sloshnost"] == 3:
        answer_s1 = random.choice(list(r))
        await state.update_data(answer_s = answer_s1)
        await state.update_data(answer_z = r[answer_s1])
    if user_data["sloshnost"] == 4:
        answer_s1 = random.choice(list(e))
        await state.update_data(answer_s = answer_s1)
        await state.update_data(answer_z = e[answer_s1])
    await message.answer_photo(photo=answer_s1)

@dp.message(F.text)
async def answer_svo(message: Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text.lower() == user_data["answer_z"]:
        await message.answer("Правильно! /get_photo")
    else:
        await message.answer("Неправильно, попробуйте еще раз или /get_photo")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())