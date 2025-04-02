import json


def get_cities(file_path: str = "data.json", city_id: int | None = None) -> list[dict] | dict:
    with open(file_path, 'r', encoding="utf-8") as fp:
        cities = json.load(fp).get("cities", [])

        if city_id is not None and 0 <= city_id < len(cities):
            return cities[city_id]
        return cities
