price = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
price_d = []

print("Список цен на товары:", sep='/n') #Вывести на экран эти цены через запятую в одну строку
for i in range(len(price)):
    print(f"{int(price[i] * 100) // 100} руб {int(price[i] * 100) % 100:0>2d} коп,", end=' ')
print(sep='/n')

print("Список цен", price)
print(sep='/n')

sorted(price)
print("Список цен по возрастанию: ", sorted(price), end=', ')
print(sep='/n')

print("Список цен", price, end=' ')
print(sep='/n')

print(sep='/n')
price.sort(reverse=True)

price_d = price[:]

print("Список цен по убыванию: ", price_d, id(price_d), end=', ')
print(sep='/n')
print("Список цен", price, id(price), end=' ')
print(sep='/n')

print("Пять самых дорогих товаров: ", price_d[:5])
