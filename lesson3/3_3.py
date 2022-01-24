import pprint

import args as args


def thesaurus(*args):

    name = []

    for i in args:
        name.append(i)

    my_dict = dict()

    for i in range(len(name)):
        key = name[i][:1]
        my_dict.setdefault(key,list())
        my_dict[key].append(name[i])

    return(my_dict)



# печать ключ/значение с новой строки
pprint.pprint(thesaurus("Иван", "Мария", "Петр", "Илья", "Дима", "Гена", "Полина", "Глеб"))

