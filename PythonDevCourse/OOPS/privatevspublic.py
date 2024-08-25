class PlayerCharacter:

    membership = True  # Class object attribute, it is static not dynamic like name age

    def __init__(self, name, age):
        if self.membership:  # OR PlayerCharacter.membership, both will work
            self._name = name  # attributes/properties _name indicates private variable
            self._age = age  # _age indicates private variable

    def run(self):
        print('run')

    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")


player1 = PlayerCharacter("eto", 100)
player1.name = 'ola'  # dynamic attribute assignment
player1.speak = 'chapak'

print(player1.speak)
print(player1.name)
print(player1._age)
print(player1._name)
