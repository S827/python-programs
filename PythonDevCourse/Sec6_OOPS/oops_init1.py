class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=20):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        return f"My name is {self.name} and I am {self.age} yeas old, also {PlayerCharacter.membership}"

    def run(self, hello):
        return f"{hello}, {self.name}"

# when object is instantiated __init__ will be called everytime.


player1 = PlayerCharacter()
print(player1)
print(player1.shout())
print(player1.run('Namaste'))
player2 = PlayerCharacter('Eto', 32)
print(player2.shout())
print(player2.run('Hola!'))
