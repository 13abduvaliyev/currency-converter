import os, json
import requests
from pprint import pprint
from url import URL

valuta = requests.get(URL)
valuta_json = valuta.json()

print("--- Bankimizga xush kelibsiz! --- ")
print(f"Mavjud valutalar: USD, EUR, RUB, UZS va boshqalar.")


sum_1 = float(input("Summani kiriting: "))
v_to = str.upper(input("Qaysi valutadan konver qilmoqchisiz: "))
v_from = str.upper(input("Qaysi valutaga konver qilmoqchisiz: "))

for i in valuta_json:
    if i['code'] == v_to:
        for j in valuta_json:
            if v_from == j['code']:
                print(f"Natija: {sum_1} {v_to} = {float(i['cb_price'])/float(j['cb_price']) * sum_1} {v_from}")
        break
                





