cube_list = []
sum_list = []
# заполнение списка кубами нечетных чисел от 0 до 1000
for number in range(1, 1000):
    if number % 2 != 0:
        cube_list.append(number ** 3)
print("список: кубы нечетных чисел в диапазоне от 0 до 1000", cube_list, sep="\n")

for i in range(len(cube_list)):
    d = 1
    b = 0
    a = cube_list[i]

# определив длину числа находим сумму его цифр
    while (a // d) !=0:
        b = b + (a // d % 10)
        d = d * 10

#новый список заполняем числами сумма цифр которых делиться нацело на 7
    if b % 7 == 0:
       sum_list.append(cube_list[i])
print("Сумма чисел из списка, сумма цифр которых делиться на 7: ", sum(sum_list))

