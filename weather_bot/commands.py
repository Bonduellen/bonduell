
from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand

CITY_COMMAND = Command('cities')
START_COMMAND = Command('start')
MY_LOCATION_COMMAND = Command('my_location')
CHANGE_MY_LOCATION_COMMAND = Command("chanche_my_location")
WEATHER_COMMAND = Command("weather")

CITY_BOT_COMMAND = BotCommand(command='cities', description="Перегляд списку міст")
START_BOT_COMMAND = BotCommand(command='start', description="Почати розмову")
MY_LOCATION_BOT_COMMAND = BotCommand(command='my_location', description="Заповнення особистого міста для отримання інформації про погоду")
CHANGE_MY_LOCATION_BOT_COMMAND = BotCommand(command='change_my_location', description="Зміна особистого міста для автоматичного отримання інформації про погоду")
WEATHER_BOT_COMMAND = BotCommand(command="weather", description="погода")