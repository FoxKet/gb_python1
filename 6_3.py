import json
import sys

with open('users.csv', 'r', encoding='utf-8') as file_user:
    user = file_user.readlines()

with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
    hobby = file_hobby.readlines()

    if len(user) < len(hobby): # если ФИО меньше хобби выходим с 1
        sys.exit(1)

    for i in range(len(user)):
        user[i] = user[i].replace(',', ' ').replace('\n', '')
    for i in range(len(hobby)):
        hobby[i] = hobby[i].replace('\n', '')
    #print(type(user), user, hobby)


    my_dict = dict(zip(user, [hobby[i] if i < len(hobby) else None for i in range(len(user))]))
    print(type(my_dict), my_dict)


    with open('dict.csv', 'w+', encoding='utf-8') as file_dict:
        file_dict.writelines(json.dumps(my_dict, indent=4, sort_keys=True, ensure_ascii=False))