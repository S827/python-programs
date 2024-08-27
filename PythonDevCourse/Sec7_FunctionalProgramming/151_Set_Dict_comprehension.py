# SET COMPREHENSION IS SIMILAR TO LISTS
# UNORDERED AND UNIQUE VALUES ONLY
my_set = {item for item in 'hello'}
print(my_set)

# using SET comprehension range of num from 0 to 99
my_set1 = {num for num in range(0, 99)}
print(my_set1)

# multiple of 2
my_set2 = {num * 2 for num in range(0, 99)}
print(my_set2)

# sqaure the range of 0 to 99 and get only even numbers
my_set3 = {num**2 for num in range(0, 99) if num % 2 == 0}
print(my_set3)


# DICTIONARY COMPREHENSION
simp_dict = {
    'a': 1,
    'b': 2
}
simp_dict_1 = {k: v**2 for k, v in simp_dict.items()}
print(simp_dict_1)

# in simple_dict, sqaure the values and only include even value in dictionary
simp_dict_2 = {k: v**2 for k, v in simp_dict.items() if v % 2 == 0}
print(simp_dict_2)

# with list [1,2,3] create dictinary using dict comprehension with lsit items as keys and item * 2 is value of that key
my_dict = {}
a = [1, 2, 3]
my_dict1 = {i: i*2 for i in a}
print(my_dict1)
for i in a:
    my_dict[i] = i * 2
print(my_dict)
