import json

from datetime import datetime

from dateutil.parser import parse

from database.db import collection

GROUP_FORMAT_TYPES: dict = {
    "month": "%Y-%m-01T00:00:00",
    "day": "%Y-%m-%dT00:00:00",
    "hour": "%Y-%m-%dT%H:00:00",
}


async def agg_sal(dt_from: str, dt_upto: str, group_type: str) -> str:
    """
    Функция для агрегирования данных в БД MongoBD на основе входных данных.
    :param dt_from: Дата начала агрегации.
    :param dt_upto: Дата завершения агрегации.
    :param group_type: Тип группировки ('month', 'day', 'hour').
    :return: Словарь аггрегированных данных из БД MongoDB.
    """

    dt_from: datetime = parse(dt_from)
    dt_upto: datetime = parse(dt_upto)
    dt_format: str = GROUP_FORMAT_TYPES.get(group_type)

    pipe = [
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {"$group": {
            "_id": {
                "$dateToString": {"format": dt_format, "date": "$dt"}
            },
            "total": {"$sum": "$value"},
        }},
        {"$sort": {"_id": 1}},
    ]

    cursor = collection.aggregate(pipe)
    results = await cursor.to_list(length=None)

    dataset = [result['total'] for result in results]
    labels = [result['_id'] for result in results]

    return json.dumps({"dataset": dataset, "labels": labels})
