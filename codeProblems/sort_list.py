def sort_list(a):
    return sorted(a)  # for descending order, pass argument of reverse = True

if __name__ == '__main__':
    a = list(map(int, input().split()))
    sorted_list = sort_list(a)
    print(sorted_list)