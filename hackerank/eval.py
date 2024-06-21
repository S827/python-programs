if __name__ == "__main__":
    # take input
    stri = input()
    # calcualte the input string using eval function
    calc = eval(stri)
    # as inbuild functions may return None so check if it no None print the calcualte result
    if calc is not None:
        print(calc)