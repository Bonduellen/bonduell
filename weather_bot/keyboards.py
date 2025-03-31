from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class WeatherCallback(CallbackData, prefix="weather"):
    id: int
    name: str

def weather_keyboard_markup(weather_list: list[dict]):

    builder = InlineKeyboardBuilder()

    for weather_data in weather_list:
        # Создаём объект CallbackData
        callback_data = WeatherCallback(id=weather_data["id"], name=weather_data["name"])
        # Добавляем кнопку в клавиатуру
        builder.button(
            text=weather_data["name"],
            callback_data=callback_data.pack()
        )

    builder.adjust(1)  # Убираем repeat=True
    return builder.as_markup()