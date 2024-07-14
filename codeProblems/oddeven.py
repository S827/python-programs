def checkEvenOdd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    a = int(input())
    check = checkEvenOdd(a)
    print(check)