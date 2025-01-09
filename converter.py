import json, os
import requests

[
    {
        "title": "BAA dirhami",
        "code": "AED",
        "cb_price": "3529.26",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Avstraliya dollari",
        "code": "AUD",
        "cb_price": "8064.27",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Kanada dollari",
        "code": "CAD",
        "cb_price": "9024.00",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Shveytsariya franki",
        "code": "CHF",
        "cb_price": "14215.35",
        "nbu_buy_price": "14000.00",
        "nbu_cell_price": "14700.00",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Xitoy yuani",
        "code": "CNY",
        "cb_price": "1768.17",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Daniya kronasi",
        "code": "DKK",
        "cb_price": "1792.92",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Misr funti",
        "code": "EGP",
        "cb_price": "255.96",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Yevro",
        "code": "EUR",
        "cb_price": "13377.80",
        "nbu_buy_price": "13240.00",
        "nbu_cell_price": "13420.00",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Angliya funt sterlingi",
        "code": "GBP",
        "cb_price": "16140.21",
        "nbu_buy_price": "15950.00",
        "nbu_cell_price": "16650.00",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Islandiya kronasi",
        "code": "ISK",
        "cb_price": "92.07",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Yaponiya iyenasi",
        "code": "JPY",
        "cb_price": "81.96",
        "nbu_buy_price": "70.00",
        "nbu_cell_price": "85.00",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Koreya respublikasi voni",
        "code": "KRW",
        "cb_price": "8.88",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Quvayt dinori",
        "code": "KWD",
        "cb_price": "42033.01",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Qozog'iston tengesi",
        "code": "KZT",
        "cb_price": "24.63",
        "nbu_buy_price": "15.00",
        "nbu_cell_price": "25.00",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Livan funti",
        "code": "LBP",
        "cb_price": "0.14",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Malayziya ringgiti",
        "code": "MYR",
        "cb_price": "2879.06",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Norvegiya kronasi",
        "code": "NOK",
        "cb_price": "1143.48",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Polsha zlotiysi",
        "code": "PLN",
        "cb_price": "3136.53",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Rossiya rubli",
        "code": "RUB",
        "cb_price": "123.68",
        "nbu_buy_price": "110.00",
        "nbu_cell_price": "130.00",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Shvetsiya kronasi",
        "code": "SEK",
        "cb_price": "1162.32",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Singapur dollari",
        "code": "SGD",
        "cb_price": "9483.49",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Turkiya lirasi",
        "code": "TRY",
        "cb_price": "366.34",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "Ukraina grivnasi",
        "code": "UAH",
        "cb_price": "306.92",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "09.01.2025 12:00:00"
    },
    {
        "title": "AQSh dollari",
        "code": "USD",
        "cb_price": "12962.98",
        "nbu_buy_price": "12920.00",
        "nbu_cell_price": "13000.00",
        "date": "09.01.2025 12:00:00"
    }
]

print("* O'ZBEKISTON MILLIY BANKIDA XUSH KELIBSIZ !!! *")
v1 = input("Qaysi valyutadan konvertatsiya qilmoqchisiz: ")
v2 = input("Qaysi valyutaga konvertatsiya qilmoqchisiz: ")




