from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token='5880390298:AAE3ploZNlpnYUzyIy1dIzHBbjYD9cMQ5ME')
dp = Dispatcher(bot)

# Welcome
button1 = KeyboardButton('Tanya')
button2 = KeyboardButton('Info')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

# Pertanyaan
button3 = KeyboardButton('ETilang')
button4 = KeyboardButton('Bayar')
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4)

# Welcome
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
     await message.reply("Hallo! Im E-Bot, Ada yang bisa dibantu??", reply_markup=keyboard1)

# Tanya
@dp.message_handler(commands=['tanya'])
async def tanya(tymessage: types.Message):
     await tymessage.reply("Mau tanya apa nih??", reply_markup=keyboard2)

# answer welcome
@dp.message_handler()
async def kb_answer(message: types.Message):
     if message.text == 'Tanya':
          await message.answer('Klik /tanya')
     elif message.text == 'Info':
          await message.answer('Klik /info')
     elif message.text == 'ETilang':
          await message.answer('E-Tilang adalah ...')
     elif message.text == 'Bayar':
          await message.answer('Cara Bayar Tilang ...')

     else:
          await message.answer(f'Pesan anda untuk /start adalah : {message.text}')

executor.start_polling(dp)
print('bot running')
