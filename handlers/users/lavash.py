from aiogram import types
from keyboards.default.lavash import *
from keyboards.inline.lavash import lavashbtn,lavashbtn2,lavashbtn3,lavashbtn4,lavashbtn5
from loader import dp

@dp.message_handler(text="Mol goʼshtidan qalampir lavash")
async def lavash654098(message: types.Message):
    await message.answer_photo(photo=open('lavash1.jpg', 'rb'), caption="""Qarsildoq chipslar, yangi bodring va pomidorlar bilan lavashga oʼralgan yumshoq mol goʼshti, bizning taʼmi oʼtkir qayla bilan
Narxi: 26 000 so'm""", reply_markup=lavashbtn)

@dp.message_handler(text="Tovuq goʼshtli qalampir lavash")
async def tuvuqlavash898(message: types.Message):
    await message.answer_photo(photo=open('lavash2.jpg', 'rb'), caption="""Yangi bodring va pomidorlar, qarsildoq chipslar bilan lavashga oʼralgan qovurilgan tovuq filesi, bizning taʼmi oʼtkir maxsus qayla bilan
Narxi: 24 000 so'm""", reply_markup=lavashbtn)

@dp.message_handler(text="Mol goʼshtidan pishloqli lavash Standard")
async def molgoshtstandartlavash(message: types.Message):
    await message.answer_photo(photo=open('lavash3.jpg', 'rb'), caption="Tanlang:", reply_markup=lavashbtn2)

@dp.message_handler(text="Lavash cheese tovuq go'sht Standart")
async def lavashcheesseed(message: types.Message):
    await message.answer_photo(photo=open('lavash4.jpg', 'rb'), caption="Tanlang:", reply_markup=lavashbtn3)

@dp.message_handler(text="FITTER")
async def fitertert(message: types.Message):
    await message.answer_photo(photo=open('lavash5.jpg', 'rb'), caption="""Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring va pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan
Narxi: 22 000 so'm""", reply_markup=lavashbtn)

@dp.message_handler(text="Lavash tovuq go'sht")
async def lavashtovuqgosht(message: types.Message):
    await message.answer_photo(photo=open('lavash6.jpg', 'rb'), caption="Tanlang:", reply_markup=lavashbtn4)

@dp.message_handler(text="Lavash mol go'sht")
async def lavashmolgosht(message: types.Message):
    await message.answer_photo(photo=open('lavash7.jpg', 'rb'), caption="Tanlang:", reply_markup=lavashbtn5)

