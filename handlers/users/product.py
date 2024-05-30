from aiogram import types
from keyboards.default.lavash import lavash
from keyboards.default.setlar import setlar
from keyboards.default.usersbutton import obsh
from loader import dp

@dp.message_handler(text='Setlar (8)')
async def set(message: types.Message):
    await message.answer_photo(photo=open('evos3.jpg', 'rb'), reply_markup=setlar)

@dp.message_handler(text='Lavash (9)')
async def lavash7777(message: types.Message):
    await message.answer_photo(photo=open('evos4.jpg', 'rb'), reply_markup=lavash)

@dp.message_handler(text='Shaurma (4)')
async def shau(message: types.Message):
    await message.answer_photo(photo=open('shaurma.jpg', 'rb'))

@dp.message_handler(text='Hot dog (8)')
async def hot(message: types.Message):
    await message.answer_photo(photo=open('hot.jpg', 'rb'))

@dp.message_handler(text='Burger (4)')
async def bur(message: types.Message):
    await message.answer_photo(photo=open('burger.jpg', 'rb'))

@dp.message_handler(text='Ichimliklar (11)')
async def ichim(message: types.Message):
    await message.answer_photo(photo=open('ichimliklar.jpg', 'rb'))

@dp.message_handler(text='Shirinlik va disertlar (4)')
async def desert(message: types.Message):
    await message.answer_photo(photo=open('desert.jpg', 'rb'))

@dp.message_handler(text='Garnirlar (10)')
async def garnir(message: types.Message):
    await message.answer_photo(photo=open('garnir.jpg', 'rb'))

@dp.message_handler(text='🔙Orqaga qaytish')
async def qayt(message: types.Message):
    await message.answer("Tanlng:", reply_markup=obsh)

