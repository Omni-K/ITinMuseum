from aiogram import Bot, Dispatcher, executor, types


# it_hackathon_bot
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def fnc_start(message: types.Message):
    await message.reply('Здравствуйте!')


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    await message.photo[-1].download()


executor.start_polling(dp)