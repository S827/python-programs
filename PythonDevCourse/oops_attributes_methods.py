class PlayerCharacter:

    membership = True  # Class object attribute, it is static not dynamic like name age

    def __init__(self, name, age):
        if self.membership:  # OR PlayerCharacter.membership, both will work
            self.name = name  # attributes/properties
            self.age = age

    def shout(self):
        return f"My name is {self.name} and I am {self.age} yeas old, also {PlayerCharacter.membership}"

    def run(self, hello):
        return f"{hello}, {self.name}"


player1 = PlayerCharacter('Eto', 32)
player2 = PlayerCharacter('Svn', 22)

print(player1.shout())
print(player2.shout())
print(player1.run('Hi'))
