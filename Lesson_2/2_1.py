# вариант 1 - напрямую
print(type(15 * 3), type(15 / 3), type(15 // 2), type(15 ** 2))

# вариант 2 - перебором
a = (15*3, 15/3, 15//2, 15**2)
#print(type(a))
for i in range(len(a)):
    print(type(a[i]))