import sys


with open('bakery.csv', "r", encoding="utf-8") as price_list:

    for price in price_list:
        print(price.replace("\n", ""))