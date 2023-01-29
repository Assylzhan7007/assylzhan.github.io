from aiogram import Bot, Dispatcher, executor, types

HELP_TEXT = """
1 /start
2 /help

"""

START_TEXT = """
<em>Біздің Телеграм-ботқа қош келдіңіздер!</em>
<b>Чат-боттың барлық мүмкіндіктерімен танысу үшін \n /help командасын жазыңыз</b>
<a href="http://htmlbook.ru/html/a">Толық ақпарат үшін мынаны басыңыз!</a>
"""
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands='help')
async def echo(message: types.Message):
	if message.text:
		await message.answer(text=HELP_TEXT)
		await message.delete()

@dp.message_handler(commands='start')
async def echo(message: types.Message):
	if message.text:
		await message.answer(text=START_TEXT, parse_mode="HTML")
		await message.delete()

@dp.message_handler(commands='description')
async def echo(message: types.Message):
	if message.text:
		await message.answer(text=DESCRIPTION_TEXT)
		await message.delete()

if __name__ == '__main__' :
	executor.start_polling(dp)
