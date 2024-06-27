def stringMutation(string, position, character):
    # convert string into list
    ls = list(string)
    # assign new char at position
    ls[position] = character
    # convert list into string again
    return ''.join(ls)

if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = stringMutation(s, int(i), c)
    print(s_new)