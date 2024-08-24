class PlayerCharacter:

    membership = True  # Class object attribute, it is static not dynamic like name age

    def __init__(self, name, age):
        if self.membership:  # OR PlayerCharacter.membership, both will work
            self.name = name  # attributes/properties
            self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Eto', 32)
player2 = PlayerCharacter('Svn', 33)

print(player1.membership)
print(player2.membership)
print(player1.name)
print(player1.age)

print(player2.name)
print(player2.age)
print(player2.run())

print(player1)
print(player2)

player2.attack = 50
print(player2.attack)

# help(player1)
# help(list)
