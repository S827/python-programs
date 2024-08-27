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
