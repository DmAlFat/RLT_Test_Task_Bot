import json

from datetime import datetime

from aiogram.filters import Filter
from aiogram.types import Message


class JSON_filter(Filter):
    def __init__(self):
        pass

    async def __call__(self, message: Message) -> bool:
        try:
            if not (str(message.text).startswith('{') and str(message.text).endswith('}')):
                return True
            else:
                return False
        except json.decoder.JSONDecodeError:
            return True


class Format_JSON_filter(Filter):
    def __init__(self):
        pass

    async def __call__(self, message: Message) -> bool:
        try:
            input_data = json.loads(str(message.text))
            if len(input_data) == 3 and \
                    all(key in input_data for key in ("dt_from", "dt_upto", "group_type")) and \
                    datetime.fromisoformat(input_data["dt_from"]) and \
                    datetime.fromisoformat(input_data["dt_upto"]) and \
                    (input_data["group_type"] in ['hour', 'day', 'month']):
                return True
        except Exception:
            return False
