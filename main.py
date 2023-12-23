"""Домашнє завдання #5
Напишіть консольну утиліту, яка повертає курс EUR та USD ПриватБанку протягом 
останніх кількох днів. Встановіть обмеження, що в утиліті можна дізнатися 
курс валют не більше, ніж за останні 10 днів. 
Для запиту до АПІ використовуйте Aiohttp client. 
Дотримуйтесь принципів SOLID під час написання завдання. 
Обробляйте коректно помилки при мережевих запитах."""

import logging
import platform
import asyncio
import aiohttp

from date_processing import list_dates
from json_output import data_output
from parsing import parser


async def index(session, _date):
    url = "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + _date
    async with session.get(url) as response:
        print("receiving data for:", _date)
        try:
            if response.status == 200:
                return await response.json()
            logging.error(f"Error status {response.status} for {url}")
        except aiohttp.ClientConnectionError() as e:
            logging.error(f"Connection error {url} as {e}")
        return None


async def gather_session(dates):
    async with aiohttp.ClientSession() as session:
        _session_list = []
        for _date in dates:
            _session_list.append(index(session, _date))

        return await asyncio.gather(*_session_list, return_exceptions=True)
        # return await asyncio.gather(*_session_list)


def main():
    currencies = ["EUR", "USD"]

    _date, _days = parser()

    dates = list_dates(_date, _days)
    # print("wait please...")

    result = asyncio.run(gather_session(dates))
    for _data in result:
        data_output(_data, currencies)


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    main()
