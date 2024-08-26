# MRO METHOD RESOLUTION ORDER
# MRO used DEAPTH FIRST SEARCH ALGORITHM
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1
    # pass


class D(B, C):
    pass


print(D.num)
print(D.mro())
print(D.__str__)
