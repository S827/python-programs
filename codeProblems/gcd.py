import math
def gcd(a, b):
    while(True):
        r = a - b * (a // b)
        if r == 0:
            return b
        else:
            a = b
            b = r

if __name__ == '__main__':
    a, b = map(int, input().split())
    res = gcd(a, b)
    print(res)

'''
gcd of 121, 143
121 = 11 * 11
143 = 11 * 13
'''