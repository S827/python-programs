def splitJoin(a):
    ls = a.split(" ")
    return "-".join(ls)


if __name__ == "__main__":
    a = input()
    res = splitJoin(a)
    print(res)