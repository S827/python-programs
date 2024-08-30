print(__name__)

import random
def randomFunc():
    print(random.random())
    print(random.randint(1, 10))
    print(random.choice([1,2,3,4,5,6]))
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    random.shuffle(my_list)
    print(my_list)
randomFunc()