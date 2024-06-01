from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.usersbutton import contact
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp
from keyboards.default.product import menyu



class Every(StatesGroup):
    habar = State()


@dp.message_handler(text='🍴 Menyu')
async def menyu1123(message: types.Message):
    await message.answer('Tanlang:', reply_markup=menyu)


@dp.message_handler(text='📋 Mening buyurtmalarim')
async def buyurtmalarim(message: types.Message):
    await message.answer('⛔️ Buyurtma mavjud emas!')


@dp.message_handler(text='📥 Savat')
async def savat(message: types.Message):
    await message.answer("🛒 Savatingiz bo'sh 🗑")


@dp.message_handler(text='📞 Aloqa')
async def aloqa(message: types.Message):
    await message.answer_photo(photo=open('images/evos.jpg', 'rb'), caption='''
Kontaktlar
Call-центр

+998 71-203-12-12
+998 71-203-55-55
Yetkazib berish telefon raqamlar:

Toshkent
+998 71-203-12-12
Namangan
+998 78-147-12-12
Farg`ona
+998 73-249-12-12
Qo`qon
+998 73-542-78-78
Andijon
+998 74-224-12-12
Samarqand
+998 78-129-16-16
Qarshi
+998 78-129-17-17
    ''')


@dp.message_handler(text='⚙️ Sozlamalar')
async def sozlamalar(message: types.Message, state: FSMContext):
    await message.answer("📋 | Sozlamalar bo'limiga xush kelibsiz!")


@dp.message_handler(text='📨 Xabar yuborish')
async def xabar(message: types.Message):
    await message.answer('Xabaringizni yozing:')
    await Every.habar.set()


@dp.message_handler(state=Every.habar)
async def habar_uchun(message: types.Message,state : FSMContext):
    await message.answer('Sizning xabaringiz qabul qilindi')
    print(message.text)
    await state.finish()


@dp.message_handler(text='ℹ️ Biz haqimizda')
async def bizhaqimizda(message: types.Message):
    await message.answer_photo(photo=open('images/evos2.jpg', 'rb'), caption='''
Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib kelmoqdaligini bilarmidingiz? 
15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 60 dan ortiq restoranlarni, o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni o‘z ichiga oladi.
    
https://evos.uz/uz/about/    
    ''')

