import pprint
import random
from typing import List


def get_jokes(n, rep):
    """
    создает набор из случайной выборки слов из трех списков
    :param n - количество шуток:
           rep - повтор слов разрешен (True), запрещен (False)
    :return - список  шуток:

    """

    list_jokes = []

    i = 0
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


    if rep:
        while i < n:
            list_jokes.append((random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives)))
            i += 1

    elif n <= 5:

        my_nouns = random.sample(nouns, n)
        my_adverbs = random.sample(adverbs, n)
        my_adjectives = random.sample(adjectives, n)

        list_jokes = list(zip(my_nouns, my_adverbs, my_adjectives))

    else:
        my_nouns = random.sample(nouns, 5)
        my_adverbs = random.sample(adverbs, 5)
        my_adjectives = random.sample(adjectives, 5)

        list_jokes = list(zip(my_nouns, my_adverbs, my_adjectives))

        list_jokes.append(["Шуток", "больше", "нет"])



    return list_jokes


pprint.pprint(get_jokes(5, True))

