class User():  # user parenthesis in class declaration to make the class to be able to be inherited in other classes
    def sign_in(self):
        return ('Logged in')


class Wizard(User):  # by passign class name as argument in class declaration, it means wizard class will inherit User class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):  # SHARED METHOD IN WIZARD AND ARCHER CLASS WHICH ACTS DIFFERENTLY WHEN CALLED
        # User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):  # Archer class will inherit User class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        return f"attacking with arrows: arrows left- {self.num_arrows}"

    def run(self):
        return f"ran really fast"

# we want HybridBorg to inherit all the above methods


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)  # to access Archer's check_arrows
        Wizard.__init__(self, name, power)  # to access Wizard's attack method


hb1 = HybridBorg('borgie', 50, 100)
print(hb1.run())
# to access Archer check_arrows need to call Archer's init in HybridBorg init method
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
