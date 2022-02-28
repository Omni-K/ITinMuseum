from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from random import randint


# it_hackathon_bot
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bot = Bot(token=token, parse_mode='MarkdownV2')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def fnc_start(message: types.Message):
    await message.reply('Здравствуйте!')


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    await message.photo[-1].download()


@dp.message_handler(commands='kotletki')
async def cmd_kotletki(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Макарошки'
    btn2 = 'Пюрешка'
    keyboard.add(btn1)
    keyboard.add(btn2)
    await message.answer('С чем котлетки?', reply_markup=keyboard)


@dp.message_handler(Text(equals='Макарошки'))
async def makaroshki_reply(message: types.Message ):
    await message.reply('Ты не шаришь', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals='Пюрешка'))
async def pureshka_reply(message: types.Message ):
    await message.reply('Ну конечно же', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands='rnd')
async def cmd_rnd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn_one = types.InlineKeyboardButton(text='Get Random Int!', callback_data='rnd_data')
    keyboard.add(btn_one)
    await message.answer('Нажми на кнопку, получишь результат', reply_markup=keyboard)

@dp.callback_query_handler(text='rnd_data')
async def send_random_int(call: types.CallbackQuery):
    await call.answer(str(randint(1, 100)))


@dp.message_handler(commands='makemecool')
async def cmd_mmc(message: types.Message):
    await message.answer('Здорова \U0001F600')


@dp.message_handler(commands='makemecool2')
async def cmd_mmc2(message: types.Message):
    await message.answer('Смотри как круто выглядит текст *жирный*, _курсив_ и `моно`')


@dp.message_handler(commands='makemecool3')
async def cmd_mmc3(message: types.Message):
    user_id = message.from_user.id
    await bot.send_sticker(user_id, 'CAACAgIAAxkBAAEEBeViHPIdpImvQ0g2N6zBWPOO8pT48QAC9AADVp29ChFYsPXZ_VVJIwQ')


executor.start_polling(dp)