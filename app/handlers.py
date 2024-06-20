from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from json import loads

from database.agg import agg_sal

from app.filters import Format_JSON_filter, JSON_filter

router = Router()


@router.message(CommandStart())
async def welcome(message: Message):
    await message.answer(
        text="Добро пожаловать в телеграм-бот для агрегации статистических данных о зарплатах сотрудников компании по "
             "временным промежуткам.\n "
             "Для получения справочной информации о работе бота отправьте команду - '/help'.")


@router.message(Command('help'))
async def cmd_help(message: Message):
    help_txt = """
    Пример входных данных:
    {
    "dt_from":"2022-09-01T00:00:00",
    "dt_upto":"2022-12-31T23:59:00",
    "group_type":"month"
    }"""
    await message.answer(text=help_txt)


@router.message(JSON_filter())
async def invalid_message_handler(message: Message):
    attention = """Невалидный запрос. Пример запроса: {"dt_from": "2022-09-01T00:00:00", "dt_upto":
    "2022-12-31T23:59:00", "group_type": "month"} """
    await message.answer(attention)


@router.message(Format_JSON_filter())
async def valid_JSON_message_handler(message: Message):
    request: dict = loads(message.text)
    answer = await agg_sal(**request)
    await message.answer(answer)


@router.message(~Format_JSON_filter())
async def invalid_JSON_message_handler(message: Message):
    attention = """Допустимо отправлять только следующие запросы:
    {"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}
    {"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}
    {"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}"""
    await message.answer(attention)
