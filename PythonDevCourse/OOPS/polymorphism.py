# PLOYMORPHISM: MANY FORMS
# METHODS BELONG TO OBJECTS
# WE USE SELF KEYWORD TO ACT UPON THE OBJECT THAT GOT INSTANTIATED
# IN PLOYMORPHISM, OBJECT CLASSES CAN SHARE THE SAME METHOD NAME BUT THOSE METHOD NAMES CAN ACT DIFFERENTLY
# BASED ON WHAT OBJECTS CALLS IT


# class User():  # user parenthesis in class declaration to make the class to be able to be inherited in other classes
#     def sign_in(self):
#         return ('Logged in')

# # Wizard and Archer can be called sub/children/derived classes


# class Wizard(User):  # by passign class name as argument in class declaration, it means wizard class will inherit User class
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):  # SHARED METHOD IN WIZARD AND ARCHER CLASS WHICH ACTS DIFFERENTLY WHEN CALLED
#         return f"attacking with power of {self.power}"


# class Archer(User):  # Archer class will inherit User class
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         return f"attacking with arrows: arrows left- {self.num_arrows}"


# wizard1 = Wizard('Merlin', 50)  # instantitate a Wizard object
# archer1 = Archer('Robin', 100)
# print(wizard1.attack())  # SHARED METHOD, WHEN CALLED ACTED DIFFERENTLY
# print(archer1.attack())  # SHARED METHOD, WHEN CALLED ACTED DIFFERENTLY


# def player_attack(char):
#     char.attack()


# player_attack(wizard1) #SAME FUNCTION RETURNING DIFFERNET OUTPUTS
# player_attack(archer1) #SAME FUNCTION RETURNING DIFFERNET OUTPUTS

# for char in [wizard1, archer1]:
#     print(char.attack()) #SAME FUNCTION RETURNING DIFFERNET OUTPUTS

# because of DIFFERNT OBJECTS


# CLASS METHOD OVERRIDES PARENT OR INHERITED CLASS METHODS
# ADDED attach method in User() class and when called attack method on instantitated obejct, attack method of thier classes
# will be called only and override parent class methods


class User():  # user parenthesis in class declaration to make the class to be able to be inherited in other classes
    def sign_in(self):
        return ('Logged in')

    def attack(self):
        print("Do nothing")
# Wizard and Archer can be called sub/children/derived classes


class Wizard(User):  # by passign class name as argument in class declaration, it means wizard class will inherit User class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):  # SHARED METHOD IN WIZARD AND ARCHER CLASS WHICH ACTS DIFFERENTLY WHEN CALLED
        User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):  # Archer class will inherit User class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f"attacking with arrows: arrows left- {self.num_arrows}"


wizard1 = Wizard('Merlin', 50)  # instantitate a Wizard object
archer1 = Archer('Robin', 100)
print(wizard1.attack())  # SHARED METHOD, WHEN CALLED ACTED DIFFERENTLY
print(archer1.attack())
