from aiogram import types
from keyboards.inline.setlar import button
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp

@dp.message_handler(text='Combo Plus Isituvchan (Qora choy)')
async def combo(message: types.Message):
    await message.answer_photo(photo=open('images/combo.jpg', 'rb'), caption="Narxi: 16 000 so'm", reply_markup=button)

@dp.message_handler(text='FitCombo')
async def combo1(message: types.Message):
    await message.answer_photo(photo=open('images/combo1.jpg', 'rb'), caption="Narxi: 30 000 so'm", reply_markup=button)

@dp.message_handler(text="Iftar kofte grill mol go'shtidan")
async def combo2(message: types.Message):
    await message.answer_photo(photo=open('images/combo2.jpg', 'rb'), caption="""Muborak RAMAZON oyi munosabati bilan maxsus taklif! Mol go'shtli 5 dona shirali gril-kotletlari, guruch, limon sharbati bilan boyitilgan qizil karamli salat, pomidorlar va yong'oqlardan tayyorlangan maxsus quyuq RAMAZON sousi. Iftorlik vaqtingiz uchun ideal yechim!
Narxi: 35 000 so'm""", reply_markup=button)

@dp.message_handler(text="Donar boks  mol go'shtidan")
async def combo3(message: types.Message):
    await message.answer_photo(photo=open('images/combo3.jpg', 'rb'), caption="""YANGILIK! Oq kunjut sousi ostidagi shirali grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, qizil karamdan tayyorlangan barra salatdan tashkil topgan qatlamlarning to'yimli uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 34 000 so'm""", reply_markup=button)

@dp.message_handler(text="Donar boks tovuq go'shtidan")
async def combo4(message: types.Message):
    await message.answer_photo(photo=open('images/combo4.jpg', 'rb'), caption="""YANGILIK!  Yangi, maxsus tayyorlangan teriyaki sousi, grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, limon sharbati bilan to'yintirilgan qizil karamdan tayyorlangan barra salatning noodatiy mazali uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 32 000 so'm""", reply_markup=button)

@dp.message_handler(text="COMBO+")
async def combo5(message: types.Message):
    await message.answer_photo(photo=open('images/combo5.jpg', 'rb'), caption="""Yeng yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va bir stakan Pepsi
Narxi: 16 000 so'm""", reply_markup=button)

@dp.message_handler(text="Iftar strips tovuq go'shtidan")
async def combo6(message: types.Message):
    await message.answer_photo(photo=open('images/combo6.jpg', 'rb'), caption="""Muborak RAMAZON oyi munosabati bilan maxsus taklif! Tovuqli 5 dona shirali gril-kotletlari, guruch, limon sharbati bilan boyitilgan qizil karamli salat, pomidorlar va yong'oqlardan tayyorlangan maxsus quyuq RAMAZON sousi. Iftorlik vaqtingiz uchun ideal yechim!
Narxi: 30 000 so'm""", reply_markup=button)

@dp.message_handler(text="Kids COMBO")
async def combo7(message: types.Message):
    await message.answer_photo(photo=open('images/combo7.jpg', 'rb'), caption="Narxi: 16 000 so'm", reply_markup=button)

