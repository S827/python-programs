def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

h = generator_function(2)
print(next(h))
print(next(h))
# print(next(h))
# print(next(h)) # we get error of StopIteration as it can iteration only twice, i.e. 0 and 1
