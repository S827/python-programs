def reverseStr(text):
    return text[::-1]

if __name__ == '__main__':
    text = input()
    reverse = reverseStr(text)
    print(reverse)