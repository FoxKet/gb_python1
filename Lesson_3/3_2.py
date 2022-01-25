def num_translate_adv(number):

    translation = dict({"one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь",
                               "eight":"восемь", "nine":"девять", "ten":"десять"})

    if number.istitle() and translation.get(number.lower()):
        return translation.get(number.lower()).capitalize()

    else:
        return translation.get(number.lower())



m = input("Введите число:  ")

print(num_translate_adv(m))
