class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        return f"My name is {self.name} and I am {self.age} yeas old, also {PlayerCharacter.membership}"

    def run(self):
        return self


player1 = PlayerCharacter('Eto', 32)
print(player1.run().run())
