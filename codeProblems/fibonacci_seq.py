def fibbonacci_seq(n):
    if n == 1:
        return [1]
    elif n > 1:
        fib_list = [1, 1]
        for i in range(n - 2):
            fib_list.append(fib_list[i] + fib_list[i+1])
    return fib_list

if __name__ == '__main__':
    n = int(input())
    if n > 0:
        generate_fibbonacci = fibbonacci_seq(n)
    else:
        print("Enter +ve integer")
    print(generate_fibbonacci)