# LAMBDA EXPRESSIONS:
# GENERALLY USED WHERE FUNCTION IS USED ONCE ONLY
# THEY ARE ANONYMOUS FUNCTION

from functools import reduce
# EXAMPLES
# MULTIPLY BY 2, use of map
my_list = [23, 34, 45]
print(list(map(lambda item: item*2, my_list)))

# filter odd values, USE OF FILTER
print(list(filter(lambda item: item % 2 != 0, my_list)))

# REDUCE BY SUMMING UP THE LIST
print(reduce(lambda acc, item: acc + item, my_list))

# EXERCISE: UASING LAMBDA SQUARE A LIST
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))


# EXERCISE: LIST SORTING
# a = [(10, 2), (4, 3), (9, 9), (10, -1)], sort it accoridng to 2nd item of tuples inside the list a
# corr_a = [(10, -1), (10, 2), (4, 3), (9, 9)] using lambda expressions
a = [(10, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda item: item[1]))
print(a[0][1])
