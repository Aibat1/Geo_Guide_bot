import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5976905593:AAEEZSfKf_0aP6Ez_GtinhgkhdRlNGpvfSg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


Methods = {'/Capital', '/Country', '/Population', '/Continent'}

countries = dict()
capitals = dict()
populations = dict()
continents = dict()

with open("Capital.txt", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    for line in lines:
        country, capital = line.split()
        countries[country] = capital
        capitals[capital] = country

with open("Population.txt", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    for line in lines:
        country, people = line.split()
        populations[country] = people

with open("Continent.txt", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    for line in lines:
        country, land = line.split()
        continents[country] = land


users = dict()


@dp.message_handler()
async def command(message: types.Message):
    if message.from_user.id in users:
        if message.text == '/start':
            text = "Выберите новое действие /Capital, /Country, /Population, /Continent, /help"
            await message.answer(text)
        elif message.text == '/help':
            text = "Этот бот поможет вам с географией"
            await message.answer(text)

        elif message.text in Methods:
            users[message.from_user.id] = message.text
            if message.text == '/Capital':
                text = "Введите название страны"
                await message.answer(text)
            if message.text == '/Country':
                text = "Введите название столицы"
                await message.answer(text)
            if message.text == '/Population':
                text = "Введите название страны"
                await message.answer(text)
            if message.text == '/Continent':
                text = "Введите название страны"
                await message.answer(text)

        elif users[message.from_user.id] == '/Capital':
            if message.text in countries:
                await message.answer(countries[message.text])
            else:
                text = "Такая страна отсутствует, введите название другой страны"
                await message.answer(text)
        elif users[message.from_user.id] == '/Country':
            if message.text in capitals:
                await message.answer(capitals[message.text])
            else:
                text = "Такая столицы отсутствует, введите название другой столицы"
                await message.answer(text)
        elif users[message.from_user.id] == '/Population':
            if message.text in populations:
                text = f"{populations[message.text]}"
                await message.answer(text)
            else:
                text = "Такая страна отсутствует, введите название другой страны"
                await message.answer(text)

        elif users[message.from_user.id] == '/Continent':
            if message.text in continents:
                await message.answer(continents[message.text])
            else:
                text = "Такая страна отсутствует, введите название другой страны"
                await message.answer(text)
    else:
        if message.text == '/start':
            text = "Выберите действие /Capital, /Country, /Population, /Continent, /help"
            await message.answer(text)
        elif message.text == '/help':
            text = "Этот бот поможет вам с географией"
            await message.answer(text)
        elif message.text in Methods:
            users[message.from_user.id] = message.text
            if message.text == '/Capital':
                text = "Введите название страны на английском языке с большой буквы"
                await message.answer(text)
            if message.text == '/Country':
                text = "Введите название столицы на английском языке с большой буквы"
                await message.answer(text)
            if message.text == '/Population':
                text = "Введите название страны на английском языке с большой буквы"
                await message.answer(text)
            if message.text == '/Continent':
                text = "Введите название страны на английском языке с большой буквы"
                await message.answer(text)
        else:
            text = "Wrong request"
            await message.answer(text)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)