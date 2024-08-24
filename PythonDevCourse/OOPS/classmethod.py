class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        return f"My name is {self.name} and I am {self.age} yeas old, also {PlayerCharacter.membership}"

    def run(self, hello):
        return f"{hello}, {self.name}"

    @classmethod
    def adding_things(cls, num1, num2):
        # return num1 + num2
        # cls instantiate a new object with name(1st arg) and age(2nd arg)
        return cls('Eto', num1 + num2)


# player1 = PlayerCharacter('Eto', 32)

# print(player1.adding_things(32, 32))
# print(PlayerCharacter.adding_things(32, 32)) # no need of instantiation when want to use classmethod

player2 = PlayerCharacter.adding_things(32, 1)
print(player2.age, player2.name)
