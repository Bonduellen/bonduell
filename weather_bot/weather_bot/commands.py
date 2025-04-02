
from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand

CITY_COMMAND = Command('cities')
START_COMMAND = Command('start')

BOT_COMMANDS = [
    BotCommand(command='cities', description="Перегляд списку міст"),
    BotCommand(command='start', description="Почати розмову")
]






