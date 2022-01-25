word = ("процент")

for number in range(1, 101):
    if number %10 == 1 and number // 10 != 1:
        print(number, word)
    elif 1 < number % 10 < 5 and number // 10 != 1:
         print(number, word+"а")
    else:
        print(number, word+"ов")
