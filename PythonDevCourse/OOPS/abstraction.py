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


player1 = PlayerCharacter("eto", 30)
player1.name = 'ola'
player1.shout = 'chapak'

print(player1.name, player1.shout)
print(player1.shout[0])
# print(player1.shout()) # notice, now shout method is not callable, as we have assigned a string to that attribute
