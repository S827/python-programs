# # 3. my_decorator is called with 'hello' as an argument.
# def my_decorator(func):
#     def wrap_func(x):    # 4. wrap_func is defined to take one argument 'x'.
#         print('******')  # 7. Prints the first line of asterisks.
#         # 8. Calls the original 'hello' function with the argument 'Hiiii'.
#         func(x)
#         print('******')  # 10. Prints the second line of asterisks.
#     return wrap_func     # 5. Returns the wrap_func function.


# @my_decorator
# # 2. 'hello' is passed to 'my_decorator', and hello is now replaced by wrap_func.
# def hello(greeting):
#     print(greeting)      # 9. Prints the greeting ('Hiiii').


# # 1. The hello function is called with the argument 'Hiiii'.
# hello('Hiiii')
# # 6. wrap_func is executed with 'Hiiii' as the argument.

print('modification with added parameter'.upper())

# # 3. my_decorator is called with 'hello' as an argument.


# def my_decorator(func):
#     def wrap_func(x, y):    # 4. wrap_func is defined to take one argument 'x'.
#         print('******')  # 7. Prints the first line of asterisks.
#         # 8. Calls the original 'hello' function with the argument 'Hiiii'.
#         func(x, y)
#         print('******')  # 10. Prints the second line of asterisks.
#     return wrap_func     # 5. Returns the wrap_func function.


# @my_decorator
# # 2. 'hello' is passed to 'my_decorator', and hello is now replaced by wrap_func.
# def hello(greeting, emoji):
#     print(greeting, emoji)      # 9. Prints the greeting ('Hiiii').


# # 1. The hello function is called with the argument 'Hiiii'.
# hello('Hiiii', ':)')
# # 6. wrap_func is executed with 'Hiiii' as the argument.


print('Another modification with args and kwargs'.upper())

# 3. my_decorator is called with 'hello' as an argument.


def my_decorator(func):
    # 4. wrap_func is defined to take one argument 'x'.
    def wrap_func(*args, **kwargs):
        print('******')  # 7. Prints the first line of asterisks.
        # 8. Calls the original 'hello' function with the argument 'Hiiii'.
        func(*args, **kwargs)
        print('******')  # 10. Prints the second line of asterisks.
    return wrap_func     # 5. Returns the wrap_func function.


@my_decorator
# 2. 'hello' is passed to 'my_decorator', and hello is now replaced by wrap_func.
def hello(greeting, emoji=':('):
    print(greeting, emoji)      # 9. Prints the greeting ('Hiiii').


# 1. The hello function is called with the argument 'Hiiii'.
hello('Hiiii', 'Hello')
# 6. wrap_func is executed with 'Hiiii' as the argument.
