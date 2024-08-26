# FUNCTIONAL PROGRAMMING:
# clear +understandable
# easy to extend
# easy to maintain
# memory efficient
# DRY

# 142.PURE FUNCTIONS

from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([20, 23, 233]))

# 143. MAP
my_list = [23, 34, 45]


def multiply_by2_1(item):
    return item * 2


print(list(map(multiply_by2_1, my_list)))
print(my_list)


# 144. FILTER
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# 145. ZIP
ur_list = [1, 2, 3]
our_list = [4, 5, 6]
print(list(zip(my_list, ur_list)))
print(list(zip(my_list, our_list)))
print(list(zip(my_list, ur_list, our_list)))

# 146. REDUCE


def accumalator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumalator, my_list, 0))
print(reduce(accumalator, my_list, 10))

# 147. EXERCISE


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.capitalize()


print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def pass50(item):
    return item > 50


print(list(filter(pass50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

my_numbers.extend(scores)

print(my_numbers)


def accumalator1(acc, item):
    # print(acc, item)
    return acc + item


print(reduce(accumalator1, my_numbers, 0))
