list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']


a = []
d = 0
for i in range(len(list)):
    if list[i+d].replace("-", "").replace("+", "").isdigit():

        if len(list[i+d]) == 1:
            list[i+d] = "0" + list[i+d]

        if len(list[i+d]) == 2 and (list[i+d].startswith("+") or list[i+d].startswith("-")):
            list[i + d] = list[i+d][0] + "0" + list[i+d][1]

        list[i+d] = '"' + list[i+d] + '"'


        # list.insert(i+d, '"')
        # d += 1
        # list.insert(i+d+1, '"')
        # d += 1
print(type(list))
print(list)
s = " ".join(list)
print(s)



# for i in range(len(list)):
#     a = list[i]
#
#     word = str(a)
#
# #    print(a)
# #    print(type(a))
#     print(type(list[i]))
#     print(word.isalnum())
#     print(word)
# #print(f"nums: {' '.join(list)}")
# print (' '.join(list)) # преобразуем в строку


