import asyncio

import logging
import sys
import requests

from commands import *
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import BOT_TOKEN as TOKEN
from keyboards import weather_keyboard_markup, WeatherCallback
from data import get_cities

# All handlers should be attached to the Router (or Dispatcher)

API = "674138c12636bbebbda5de3f81c3b928"


dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        f"Вітаю, {message.from_user.full_name}!\n"\
        "Я бот який допоможе нарешті узнати точну погоду в Бєльгії.",
    )


@dp.message()
async def cities(message: Message) -> None:
    if message.text == "/cities":
        data = get_cities()
        markup = weather_keyboard_markup(weather_list=data)
        await message.answer("Оберіть місто для перегляду погоди:", reply_markup=markup)


@dp.message()
async def get_weather(message: Message) -> None:
    city = message.text.strip().lower()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ua"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]

        await message.answer(f"🌤 Погода в {city.capitalize()}:\n"
                             f"🌡 Температура: {temp}°C\n"
                             f"☁️ Опис: {weather_desc}")
    else:
        await message.answer("❌ Не вдалося отримати погоду. Перевірте назву міста!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())