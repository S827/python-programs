def calcPoly(y, poly):
    # poly_str = ' '.join(poly)
    # replace the x in poly with value of y
    print(y, str(y))
    poly_str = poly.replace('x', str(y))
    # calculate the polynomail with eval function, anyting passed in eval function as string will be calcualted
    result = eval(poly_str)
    print(poly_str)
    return result

if __name__ == "__main__":
    # take input of x and result of polynomial
    x, result = map(int, input().split())
    poly = "x**3 + x**2 + x + 1"
    # call calcPoly function with args x and polynomial
    out = calcPoly(x, poly)
    print(out == result)