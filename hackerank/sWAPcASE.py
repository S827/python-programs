def swapCase(s):
    a = []
    for i in range(len(s)):
        if s[i].isupper():
            a.append(s[i].lower())
        elif s[i].islower():
            a.append(s[i].upper())
        else:
            a.append(s[i])
    return ''.join(a)

if __name__ == "__main__":
    s = input()
    result = swapCase(s)
    print(result)