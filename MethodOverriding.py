

class Base:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self):
        self.name = input("Enter Name:")
        self.age = int(input("Enter Age:"))

    def display(self):
        print("Base class display is called")
        print("Name:{0} and age:{1}".format(self.name, self.age))
base = Base("regis", 23)
base.display()


class Derived(Base):
    def __init__(self, name, age, place):
        self.place = place
        super(Derived, self).__init__(name, age)

    def display(self):
        print("CALL FROM DERIVED CLASS")
        print("Name:{0} and age:{1} and place:{2}".format(self.name, self.age, self.place))

derived = Derived("regis charles", 24, "Mumbai")
derived.display()


