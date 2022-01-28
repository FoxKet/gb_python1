#  Есть два списка:
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо
# вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)

from sys import getsizeof

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Михаил']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


#temp = [klasses[i] if i < len(klasses) else None for i in range(len(tutors))]

a = tuple(zip(tutors,[klasses[i] if i < len(klasses) else None for i in range(len(tutors))]))
print(type(a), a)

#запуск генератора и вывод всех значений
gen = (a[i] for i in range(len(tutors)))
print(type(gen), *gen)

#запуск генератора до истощения
gen = (a[i] for i in range(len(tutors)))
for i in range(len(tutors)+1):
    print(next(gen))

