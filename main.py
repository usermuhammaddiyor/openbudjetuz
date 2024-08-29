from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

bottoken = '6516879720:AAHzKaS_OVAIWu-L0Gusyk9QLWgSRD328zY'
bot = Bot(bottoken)
dp = Dispatcher(bot)

knopka = InlineKeyboardMarkup()
knopka.add(
    InlineKeyboardButton(text='Ovoz berish',
                         url='https://t.me/ochiqbudjet_07_bot?start=048346761011')
)


@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Xush kelibsiz. Ovoz berish uchun bosing⬇️",
                           reply_markup=knopka)


executor.start_polling(dp, skip_updates=True)