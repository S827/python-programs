def max_of_3(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    max = max_of_3(a, b, c)
    print(max)