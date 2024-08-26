# inntrospection: ability to determine the type of the object at runtime

class User():  # user parenthesis in class declaration to make the class to be able to be inherited in other classes
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return ('Logged in')

# Wizard and Archer can be called sub/children/derived classes


# by passign class name as argument in class declaration, it means wizard class will inherit User class
class Wizard(User):
    def __init__(self, name, power, email):
        # self.email = email # INEFFICIENT
        # here User.__init__(self, email) OR super().__init__(email) can be called also super() don't require self
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):  # SHARED METHOD IN WIZARD AND ARCHER CLASS WHICH ACTS DIFFERENTLY WHEN CALLED
        User.attack(self)
        print(f"attacking with power of {self.power}")


# instantitate a Wizard object
wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
print(wizard1.email)
print(dir(wizard1))  # check the objecct type
