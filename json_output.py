""" фільтруємо дані, виводимо дані у вигляді гарної таблиці """

from colors import GRAY, RESET, LIGHTBLUE_BACK, GRAY_BACK

TABLE_TEMPLATE = "{:^13}{:^15}{:^15}{:^15}{:^15}"
TABLE_WIDTH = 72


def _table_line(char):
    print(char * TABLE_WIDTH)
    # return


def _table_print(_date, currency_data):

    print("\nDate:", GRAY_BACK, _date, RESET)
    _table_line("=")

    print(
        GRAY,
        TABLE_TEMPLATE.format("Currency", "NBU sale", "NBU pur", "PB sale", "PB pur"),
        RESET,
    )
    for currency, entry in currency_data.items():
        _table_line("-")

        print(LIGHTBLUE_BACK, "{:^11}".format(currency), RESET, end="")
        for el in ("saleRateNB", "purchaseRateNB", "saleRate", "purchaseRate"):
            try:
                print("{:^15}".format(entry[el]), end="")
            except KeyError:
                print(GRAY, "{:^13}".format(" --- "), RESET, end="")
            if el == "purchaseRate":
                print(end="\n")

    _table_line("=")
    # return


def _data_selection(data, target_currencies):
    """'фільтрація даних"""
    currency_data = {}

    for rate in data["exchangeRate"]:
        currency_code = rate["currency"]

        if currency_code in target_currencies:
            currency_data[currency_code] = rate
    return currency_data


def data_output(data, target_currencies):
    """головна функція модуля - виводимо відфільтровані дані у вигляді таблиці"""
    _table_print(data["date"], _data_selection(data, target_currencies))
    # return


if __name__ == "__main__":
    target_currencies = ["EUR", "USD", "CAD"]

    data_3 = {
        "date": "23.12.2023",
        "bank": "PB",
        "baseCurrency": 980,
        "baseCurrencyLit": "UAH",
        "exchangeRate": [
            {
                "baseCurrency": "UAH",
                "currency": "AUD",
                "saleRateNB": 25.4114,
                "purchaseRateNB": 25.4114,
            },
            {
                "baseCurrency": "UAH",
                "currency": "AZN",
                "saleRateNB": 22.1285,
                "purchaseRateNB": 22.1285,
            },
            {
                "baseCurrency": "UAH",
                "currency": "BYN",
                "saleRateNB": 13.6655,
                "purchaseRateNB": 13.6655,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CAD",
                "saleRateNB": 28.1579,
                "purchaseRateNB": 28.1579,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CHF",
                "saleRateNB": 43.7778,
                "purchaseRateNB": 43.7778,
                "saleRate": 44.31,
                "purchaseRate": 43.72,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CNY",
                "saleRateNB": 5.2647,
                "purchaseRateNB": 5.2647,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CZK",
                "saleRateNB": 1.6864,
                "purchaseRateNB": 1.6864,
                "saleRate": 1.68,
                "purchaseRate": 1.65,
            },
            {
                "baseCurrency": "UAH",
                "currency": "DKK",
                "saleRateNB": 5.5367,
                "purchaseRateNB": 5.5367,
            },
            {
                "baseCurrency": "UAH",
                "currency": "EUR",
                "saleRateNB": 41.2846,
                "purchaseRateNB": 41.2846,
                "saleRate": 41.8,
                "purchaseRate": 40.8,
            },
            {
                "baseCurrency": "UAH",
                "currency": "GBP",
                "saleRateNB": 47.5876,
                "purchaseRateNB": 47.5876,
                "saleRate": 48.13,
                "purchaseRate": 47.5,
            },
            {
                "baseCurrency": "UAH",
                "currency": "GEL",
                "saleRateNB": 13.4518,
                "purchaseRateNB": 13.4518,
            },
            {
                "baseCurrency": "UAH",
                "currency": "HUF",
                "saleRateNB": 0.107943,
                "purchaseRateNB": 0.107943,
            },
            {
                "baseCurrency": "UAH",
                "currency": "ILS",
                "saleRateNB": 10.3995,
                "purchaseRateNB": 10.3995,
            },
            {
                "baseCurrency": "UAH",
                "currency": "JPY",
                "saleRateNB": 0.26334,
                "purchaseRateNB": 0.26334,
            },
            {
                "baseCurrency": "UAH",
                "currency": "KZT",
                "saleRateNB": 0.081863,
                "purchaseRateNB": 0.081863,
            },
            {
                "baseCurrency": "UAH",
                "currency": "MDL",
                "saleRateNB": 2.1451,
                "purchaseRateNB": 2.1451,
            },
            {
                "baseCurrency": "UAH",
                "currency": "NOK",
                "saleRateNB": 3.6494,
                "purchaseRateNB": 3.6494,
            },
            {
                "baseCurrency": "UAH",
                "currency": "PLN",
                "saleRateNB": 9.5111,
                "purchaseRateNB": 9.5111,
                "saleRate": 9.65,
                "purchaseRate": 9.25,
            },
            {
                "baseCurrency": "UAH",
                "currency": "SEK",
                "saleRateNB": 3.7183,
                "purchaseRateNB": 3.7183,
            },
            {
                "baseCurrency": "UAH",
                "currency": "SGD",
                "saleRateNB": 28.285,
                "purchaseRateNB": 28.285,
            },
            {
                "baseCurrency": "UAH",
                "currency": "TMT",
                "saleRateNB": 10.3867,
                "purchaseRateNB": 10.3867,
            },
            {
                "baseCurrency": "UAH",
                "currency": "TRY",
                "saleRateNB": 1.2894,
                "purchaseRateNB": 1.2894,
            },
            {
                "baseCurrency": "UAH",
                "currency": "UAH",
                "saleRateNB": 1.0,
                "purchaseRateNB": 1.0,
            },
            {
                "baseCurrency": "UAH",
                "currency": "USD",
                "saleRateNB": 37.5964,
                "purchaseRateNB": 37.5964,
                "saleRate": 37.8,
                "purchaseRate": 37.3,
            },
            {
                "baseCurrency": "UAH",
                "currency": "UZS",
                "saleRateNB": 0.0029561,
                "purchaseRateNB": 0.0029561,
            },
            {
                "baseCurrency": "UAH",
                "currency": "XAU",
                "saleRateNB": 76624.85,
                "purchaseRateNB": 76624.85,
            },
        ],
    }

    data = {
        "date": "22.12.2023",
        "bank": "PB",
        "baseCurrency": 980,
        "baseCurrencyLit": "UAH",
        "exchangeRate": [
            {
                "baseCurrency": "UAH",
                "currency": "AUD",
                "saleRateNB": 25.4114,
                "purchaseRateNB": 25.4114,
            },
            {
                "baseCurrency": "UAH",
                "currency": "AZN",
                "saleRateNB": 22.1285,
                "purchaseRateNB": 22.1285,
            },
            {
                "baseCurrency": "UAH",
                "currency": "BYN",
                "saleRateNB": 13.6655,
                "purchaseRateNB": 13.6655,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CAD",
                "saleRateNB": 28.1579,
                "purchaseRateNB": 28.1579,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CHF",
                "saleRateNB": 43.7778,
                "purchaseRateNB": 43.7778,
                "saleRate": 44.16,
                "purchaseRate": 43.57,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CNY",
                "saleRateNB": 5.2647,
                "purchaseRateNB": 5.2647,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CZK",
                "saleRateNB": 1.6864,
                "purchaseRateNB": 1.6864,
                "saleRate": 1.685,
                "purchaseRate": 1.655,
            },
            {
                "baseCurrency": "UAH",
                "currency": "DKK",
                "saleRateNB": 5.5367,
                "purchaseRateNB": 5.5367,
            },
            {
                "baseCurrency": "UAH",
                "currency": "EUR",
                "saleRateNB": 41.2846,
                "purchaseRateNB": 41.2846,
                "saleRate": 41.9,
                "purchaseRate": 40.9,
            },
            {
                "baseCurrency": "UAH",
                "currency": "GBP",
                "saleRateNB": 47.5876,
                "purchaseRateNB": 47.5876,
                "saleRate": 48.0,
                "purchaseRate": 47.4,
            },
            {
                "baseCurrency": "UAH",
                "currency": "GEL",
                "saleRateNB": 13.4518,
                "purchaseRateNB": 13.4518,
            },
            {
                "baseCurrency": "UAH",
                "currency": "HUF",
                "saleRateNB": 0.107943,
                "purchaseRateNB": 0.107943,
            },
            {
                "baseCurrency": "UAH",
                "currency": "ILS",
                "saleRateNB": 10.3995,
                "purchaseRateNB": 10.3995,
            },
            {
                "baseCurrency": "UAH",
                "currency": "JPY",
                "saleRateNB": 0.26334,
                "purchaseRateNB": 0.26334,
            },
            {
                "baseCurrency": "UAH",
                "currency": "KZT",
                "saleRateNB": 0.081863,
                "purchaseRateNB": 0.081863,
            },
            {
                "baseCurrency": "UAH",
                "currency": "MDL",
                "saleRateNB": 2.1451,
                "purchaseRateNB": 2.1451,
            },
            {
                "baseCurrency": "UAH",
                "currency": "NOK",
                "saleRateNB": 3.6494,
                "purchaseRateNB": 3.6494,
            },
            {
                "baseCurrency": "UAH",
                "currency": "PLN",
                "saleRateNB": 9.5111,
                "purchaseRateNB": 9.5111,
                "saleRate": 9.65,
                "purchaseRate": 9.25,
            },
            {
                "baseCurrency": "UAH",
                "currency": "SEK",
                "saleRateNB": 3.7183,
                "purchaseRateNB": 3.7183,
            },
            {
                "baseCurrency": "UAH",
                "currency": "SGD",
                "saleRateNB": 28.285,
                "purchaseRateNB": 28.285,
            },
            {
                "baseCurrency": "UAH",
                "currency": "TMT",
                "saleRateNB": 10.3867,
                "purchaseRateNB": 10.3867,
            },
            {
                "baseCurrency": "UAH",
                "currency": "TRY",
                "saleRateNB": 1.2894,
                "purchaseRateNB": 1.2894,
            },
            {
                "baseCurrency": "UAH",
                "currency": "UAH",
                "saleRateNB": 1.0,
                "purchaseRateNB": 1.0,
            },
            {
                "baseCurrency": "UAH",
                "currency": "USD",
                "saleRateNB": 37.5964,
                "purchaseRateNB": 37.5964,
                "saleRate": 37.9,
                "purchaseRate": 37.4,
            },
            {
                "baseCurrency": "UAH",
                "currency": "UZS",
                "saleRateNB": 0.0029561,
                "purchaseRateNB": 0.0029561,
            },
            {
                "baseCurrency": "UAH",
                "currency": "XAU",
                "saleRateNB": 76624.85,
                "purchaseRateNB": 76624.85,
            },
        ],
    }

    data_2 = {
        "date": "21.12.2022",
        "bank": "PB",
        "baseCurrency": 980,
        "baseCurrencyLit": "UAH",
        "exchangeRate": [
            {
                "baseCurrency": "UAH",
                "currency": "AUD",
                "saleRateNB": 24.3199,
                "purchaseRateNB": 24.3199,
            },
            {
                "baseCurrency": "UAH",
                "currency": "AZN",
                "saleRateNB": 21.5515,
                "purchaseRateNB": 21.5515,
            },
            {
                "baseCurrency": "UAH",
                "currency": "BYN",
                "saleRateNB": 13.2919,
                "purchaseRateNB": 13.2919,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CAD",
                "saleRateNB": 26.8246,
                "purchaseRateNB": 26.8246,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CHF",
                "saleRateNB": 39.3825,
                "purchaseRateNB": 39.3825,
                "saleRate": 43.0,
                "purchaseRate": 39.36,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CNY",
                "saleRateNB": 5.2471,
                "purchaseRateNB": 5.2471,
            },
            {
                "baseCurrency": "UAH",
                "currency": "CZK",
                "saleRateNB": 1.6046,
                "purchaseRateNB": 1.6046,
                "saleRate": 1.74,
                "purchaseRate": 1.6,
            },
            {
                "baseCurrency": "UAH",
                "currency": "DKK",
                "saleRateNB": 5.2175,
                "purchaseRateNB": 5.2175,
            },
            {
                "baseCurrency": "UAH",
                "currency": "EUR",
                "saleRateNB": 38.8121,
                "purchaseRateNB": 38.8121,
                "saleRate": 42.1,
                "purchaseRate": 41.1,
            },
            {
                "baseCurrency": "UAH",
                "currency": "GBP",
                "saleRateNB": 44.3705,
                "purchaseRateNB": 44.3705,
                "saleRate": 48.55,
                "purchaseRate": 44.44,
            },
            {
                "baseCurrency": "UAH",
                "currency": "GEL",
                "saleRateNB": 13.4815,
                "purchaseRateNB": 13.4815,
            },
            {
                "baseCurrency": "UAH",
                "currency": "HUF",
                "saleRateNB": 0.096026,
                "purchaseRateNB": 0.096026,
            },
            {
                "baseCurrency": "UAH",
                "currency": "ILS",
                "saleRateNB": 10.5504,
                "purchaseRateNB": 10.5504,
            },
            {
                "baseCurrency": "UAH",
                "currency": "JPY",
                "saleRateNB": 0.27556,
                "purchaseRateNB": 0.27556,
            },
            {
                "baseCurrency": "UAH",
                "currency": "KZT",
                "saleRateNB": 0.077794,
                "purchaseRateNB": 0.077794,
            },
            {
                "baseCurrency": "UAH",
                "currency": "MDL",
                "saleRateNB": 1.886,
                "purchaseRateNB": 1.886,
            },
            {
                "baseCurrency": "UAH",
                "currency": "NOK",
                "saleRateNB": 3.693,
                "purchaseRateNB": 3.693,
            },
            {
                "baseCurrency": "UAH",
                "currency": "PLN",
                "saleRateNB": 8.301,
                "purchaseRateNB": 8.301,
                "saleRate": 9.05,
                "purchaseRate": 8.3,
            },
            {
                "baseCurrency": "UAH",
                "currency": "SEK",
                "saleRateNB": 3.5085,
                "purchaseRateNB": 3.5085,
            },
            {
                "baseCurrency": "UAH",
                "currency": "SGD",
                "saleRateNB": 27.0258,
                "purchaseRateNB": 27.0258,
            },
            {
                "baseCurrency": "UAH",
                "currency": "TMT",
                "saleRateNB": 10.4482,
                "purchaseRateNB": 10.4482,
            },
            {
                "baseCurrency": "UAH",
                "currency": "TRY",
                "saleRateNB": 1.9602,
                "purchaseRateNB": 1.9602,
            },
            {
                "baseCurrency": "UAH",
                "currency": "UAH",
                "saleRateNB": 1.0,
                "purchaseRateNB": 1.0,
            },
            {
                "baseCurrency": "UAH",
                "currency": "USD",
                "saleRateNB": 36.5686,
                "purchaseRateNB": 36.5686,
                "saleRate": 40.05,
                "purchaseRate": 39.55,
            },
            {
                "baseCurrency": "UAH",
                "currency": "UZS",
                "saleRateNB": 0.0032641,
                "purchaseRateNB": 0.0032641,
            },
            {
                "baseCurrency": "UAH",
                "currency": "XAU",
                "saleRateNB": 65873.21,
                "purchaseRateNB": 65873.21,
            },
        ],
    }

    data_output(data, target_currencies)
    data_output(data_2, target_currencies)
    data_output(data_3, target_currencies)
