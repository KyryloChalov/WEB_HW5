"""розбір командної строки
    варіанти:
        - за замовчуванням (без параметрів, або параметр 'help') виводиться help та дані за сьогодні
        - якшо параметрів 2 - перший з них має бути дата, другий - кількість днів 
        - за наявності тільки одного параметру, відбувається перевірка: 
            якщо цей параметр - ціле число, воно визначається як кількість днів
            якщо ні - цей параметр вважається датою 
        - проводиться перевірка коректності введеної дати (модуль date_processing)
        - якщо кількість днів більша за 10, виводиться повідомлення про обмеження до 10 днів
    """
import sys
from datetime import date
from colors import YELLOW, CYAN, RESET
from date_processing import clear_date, ERROR_DATA


def _help():
    print(
        f"{CYAN}>>>{RESET}\tformat:{YELLOW} main <date> <days>{RESET}",
        end="\t",
    )
    print("by default, you will receive the exchange rate for today")


def parser():
    """parsing"""

    _date, _days = str(date.today()), 1  # за замовченням - лише сьогодні

    if len(sys.argv) == 1:
        _help()

    # можливий формат main <days>, для отримання курсу за <days> днів від сьогодні
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].lower() == "help":
                _help()
                # sys.exit()
            else:
                _days = int(sys.argv[1])
        except ValueError:
            _date = sys.argv[1]

    if len(sys.argv) > 2:
        _date = sys.argv[1]
        try:
            _days = int(sys.argv[2])
        except ValueError:
            ...

    if _days > 10:
        sys.exit(
            ERROR_DATA + "exchange rate request is allowed for no more than 10 days"
        )

    return clear_date(_date), _days
