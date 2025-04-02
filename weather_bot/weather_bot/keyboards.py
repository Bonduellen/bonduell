from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class WeatherCallback(CallbackData, prefix="weather", sep=";"):
    id: int
    name: str


def weather_keyboard_markup(weather_list: list[dict],  offset: int | None = None, skip: int | None = None):
    """
    Створює клавіатуру на основі отриманого списку фільмів
    Приклад використання
    >>> await message.answer(
            text="Some text",
            reply_markup=weather_keyboard_markup(cities_list)
        )
    """

    # Створюємо та налаштовуємо клавіатуру
    builder = InlineKeyboardBuilder()

    for weather_data in weather_list:
        # Создаём объект CallbackData
        callback_data = WeatherCallback(**weather_data)
        # Добавляем кнопку в клавиатуру
        builder.button(
            text=weather_data["name"],
            callback_data=callback_data.pack()
        )

    builder.adjust(1, repeat=True)  # Убираем repeat=True
    return builder.as_markup()