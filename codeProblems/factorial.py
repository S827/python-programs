def fact(n):
    f = n
    while n > 1:
        f = f * (n - 1)
        n -= 1
    return f

if __name__ == '__main__':
    n = int(input())
    fac = fact(n)
    print(fac)
