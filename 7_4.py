import os

my_dict = {}


path = 'D:\pythonProject1\lesson7\some_data'

with os.scandir(path) as files:

    for f in files:
        if os.path.isfile(f):
            size = 10 ** len(str(os.stat(f).st_size))

            my_dict[size] = my_dict.get(size, 0) + 1

print(my_dict)