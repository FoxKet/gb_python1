
import sys

price = list(map(float, sys.argv[1:]))

with open('bakery.csv', "a", encoding="utf-8") as price_list:
     print(*price, sep="\n", file=price_list)