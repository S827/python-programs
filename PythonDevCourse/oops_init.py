class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        return f"My name is {self.name} and I am {self.age} yeas old, also {PlayerCharacter.membership}"

    def run(self, hello):
        return f"{hello}, {self.name}"


# when object is instantiated __init__ will be called everytime.
# __init__ will be called while instantitating
player1 = PlayerCharacter('Eto', 32)
