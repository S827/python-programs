# INHERITENCE ALLOWS NEW OBJECTS TO TAKE ON THE PROPERTIES OF EXISTING OBJECTS, SO CLASSES CAN BE INHERITED
#

# topic 1
# class User(): # user parenthesis in class declaration to make the class to be able to be inherited in other classes
#     def sign_in(self):
#         return ('Logged in')


# class Wizard(User): #by passign class name as argument in class declaration, it means wizard class will inherit User class
#     pass


# class Archer(User): #Archer class will inherit User class
#     pass


# wizard1 = Wizard() # instantitate a Wizard object
# print(wizard1.sign_in()) # calling inherited methods of user on Wizard object


# TOPIC 2

class User():  # user parenthesis in class declaration to make the class to be able to be inherited in other classes
    def sign_in(self):
        return ('Logged in')

# Wizard and Archer can be called sub/children/derived classes


class Wizard(User):  # by passign class name as argument in class declaration, it means wizard class will inherit User class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f"attacking with power of {self.power}"


class Archer(User):  # Archer class will inherit User class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f"attacking with arrows: arrows left- {self.num_arrows}"


wizard1 = Wizard('Merlin', 50)  # instantitate a Wizard object
archer1 = Archer('Robin', 100)
print(wizard1.attack())
print(archer1.attack())
print(wizard1.sign_in())

# check instance
print(isinstance(wizard1, Wizard))
print(isinstance(archer1, Archer))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
# User is inerited from object, Wizard is inherited from User
