class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('JoJo', 2)
cat2 = Cat('Pussycat', 1)
cat3 = Cat('Dictator', 6)


# 2 Create a function that finds the oldest cat
def findOldCat(*args):
    return max(args)


oldcatage = findOldCat(cat1.age, cat2.age, cat3.age)
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldcatage} years old.")
