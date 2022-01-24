number = int(input("Введите время в секундах:  "))

# находим дни
d = number // 86400
number %= 86400
# находим часы
h = number // 3600
number %= 3600
# находим минуты
m = number // 60
number = number - m*60
# находим секунды
s = number % 60

print(d, "дн", h, "час", m, "мин", s, "сек")