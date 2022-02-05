import os
import shutil


path = r'/my_project'

#os.path.join(folder, file),    # склеиваем в полный путь
#os.path.relpath(path, start=None) - вычисляет путь относительно директории start
# (по умолчанию - относительно текущей директории).


files = [os.path.relpath(os.path.join(root, file), path) for root, _, files in os.walk(path) for file in files if file.endswith(".html")]


for path_a in files:
    p, file = os.path.split(path_a)
    path_b = os.path.join(path, "template", p)


    if not os.path.exists(path_b):
        os.makedirs(path_b)
    shutil.copyfile(os.path.join(path, path_a), os.path.join(path_b, file))