def fib(num):
    a = 0
    b = 1
    f_list = []
    for i in range(num):  # 0,1,2,3,4
        f_list.append(a)  # 0,1,1,2,3
        temp = a          # 0,1,1,2,3
        a = b             # 1,1,2,3,5
        b = temp + b      # 1,2,3,5,8
    return f_list


print(fib(20))  # 0, 1, 2, 3, 4

print('using generators'.upper())


def fib_gen(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
    return a


for x in fib_gen(20):
    print(x)
