def num_translate(number):

    translation = dict({"one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь",
                           "eight":"восемь", "nine":"девять", "ten":"десять"})

    return translation.get(number.lower())


m = input("Введите число:  ")

print(num_translate(m))



