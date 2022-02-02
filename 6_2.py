
def spammer_search(file):

    my_dict = {}

    with open('new_file.txt', 'r', encoding='utf-8') as file_n:

        for i in file_n:
            temp = i.split()
            addr = temp[0]
            if addr in my_dict:
                my_dict[addr] += 1
            else:
                my_dict[addr] = 1

        for key in my_dict:
            max_key = max(my_dict, key=my_dict.get)
            return (max_key.split(), my_dict[max_key])


if __name__ == "__main__":
    temp = spammer_search('new_file.txt')
    for i in temp:
        print(i)
