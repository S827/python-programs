def addTwoNum(a, b):
    return a + b

if __name__ == "__main__":
    a, b = map(int, input().split())
    sum = addTwoNum(a, b)
    print(sum)