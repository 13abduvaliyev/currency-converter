import os, json
import requests
from pprint import pprint
from url import URL

valuta = requests.get(URL)
valuta_json = valuta.json()

print("--- Bankimizga xush kelibsiz! --- ")
print(f"Mavjud valutalar: ", end="")
for a in valuta_json:
    print(a['code'], end=" ")


summa = float(input("\nSummani kiriting: "))
v_from = str.upper(input("Qaysi valutadan konver qilmoqchisiz: "))
v_to = str.upper(input("Qaysi valutaga konver qilmoqchisiz: "))

for i in valuta_json:
    if i['code'] == v_from:
        for j in valuta_json:
            if v_to == j['code']:
                print(f"Natija: {summa} {v_from} = {float(i['cb_price'])/float(j['cb_price']) * summa} {v_to}")
        break
                





