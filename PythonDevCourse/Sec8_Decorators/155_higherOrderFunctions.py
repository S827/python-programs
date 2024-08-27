# HIGHER ORDER FUNCTIONS HOC
# IT CAN BE A FUNCTION THAT ACEEPTS ANOTHER FUNCTION AS A PARAMETER
def greet(func):
    func()
# HOC: IF A FUNCTION RETURNS ANOTHER FUNCTION


def greet2():
    def func():
        return 5
    return func
# EXAMPLE: HOC BUILT IN HOC: .map(), .filter(), .reduce() it is a function that accepts another function


def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')
    return wrap_func


@my_decorator
def hello():
    print('hello')


hello()


def bye():
    print('see ya later')


bye()


@my_decorator  # with the help of decorator we can supercharge our normal functions like bye1 and hello functions above
def bye1():
    print('See ya later')


bye1()

# how it is happening

print('how it is happening'.upper())
hello2 = my_decorator(hello)
print(hello2())
my_decorator(hello)()  # equivalent to above
