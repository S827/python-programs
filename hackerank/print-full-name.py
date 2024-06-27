def printFullName(f, l):
    print("Hello {} {}! You just delved into Python.".format(f, l))


if __name__ == "__main__":
    first = input()
    last = input()
    printFullName(first, last)