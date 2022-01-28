# генератор нечетных чисел

def odd_nums(n):
    nums = (num for num in range(1, n + 1, 2))
    return(nums)

if __name__ == '__main__':

    a = odd_nums(15)
    print(type(a), *a)
