import pprint
import re

def fun_pars(file):

    import re

    with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1, open('new_file.txt', 'w') as file_n:

        for i in file_1:
            temp = re.split('- -|"', i)
            addr = temp[0]
            request_1 = temp[2]
            request = request_1.split()[0]
            resource = request_1.split()[1]
            yield(addr, request, resource)
            print(addr, request, resource, file=file_n)

if __name__ == "__main__":
    temp = fun_pars('nginx_logs.txt')
    for i in temp:
        print(i)