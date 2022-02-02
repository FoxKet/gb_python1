import sys
# но если в файле пустые строки или др формат - не работает
arguments = sys.argv[1:]
begin = int(arguments[0])
end = int(arguments[1])

with open('bakery.csv', "r", encoding="utf-8") as price_list:
    price = price_list.readlines()
price = ''.join(price[(begin-1):end])
print(price)