my_list = [char for char in 'hello']
print(my_list)

my_list1 = [len(item) for item in ['red', 'apple']]
print(my_list1)  # returns length of list items in list at exact item positions

# using list comprehension range of num from 0 to 99
my_list2 = [num for num in range(0, 100)]
print(my_list2)

my_list3 = [num*2 for num in range(0, 100)]  # multiple of 2
print(my_list3)

# sqaure the range of 0 to 99 and get only even numbers
my_list4 = [num**2 for num in range(0, 100)]
even_list4 = list(filter(lambda x: x % 2 == 0, my_list4))
print(even_list4)
# OR
my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list5)

my_list6 = [(num**2 % 2 == 0)
            for num in range(0, 100)]  # it returns boolean of even values
