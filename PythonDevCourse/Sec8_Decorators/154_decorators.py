# def hello():
#     print('Hellooooo')


# greet = hello
# del hello
# print(greet)
# # print(hello)  # gives error as hello is being deleted
# print(greet())
#
#
##
#
# decorators super charge our functions, and can add extra functionality
@decorator
def hello():
    pass


def hello1(func):
    func()


def greet1():
    print('Still Here')


a = hello1(greet1)
print(a)
