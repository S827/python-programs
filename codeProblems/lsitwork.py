def command(N):
    i = 0
    ls = []
    while i < N:
        com = input()
        parts = com.split()
        if len(parts) == 1:
            if com == 'print':
                print(ls)
            elif com == 'sort':
                ls.sort()
            elif com == 'pop':
                ls.pop()
            elif com == 'reverse':
                ls.reverse()
        elif len(parts) == 2:
            if parts[0] == 'remove':
                ls.remove(int(parts[1]))
            elif parts[0] == 'append':
                ls.append(int(parts[1]))
        elif len(parts) == 3:
            if parts[0] == 'insert':
                ls.insert(int(parts[1]), int(parts[2]))
        i += 1
if __name__ == '__main__':
    N = int(input())
    command(N)