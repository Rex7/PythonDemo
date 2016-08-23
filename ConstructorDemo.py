# Constructor Demo


class Demo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self):
        print("Name:{0} \n Age:{1} ".format(self.name, self.age))

    def display(self):
        print("Name:{} and age:{}".format(self.name, self.age))


class Inheritance(Demo):

    def __init__(self, per, name, age):
        self.per = per
        super(Inheritance, self).__init__(name, age)

    def display(self):
        print("\n Name:{} \n age:{} \n percentage:{}".format(self.name, self.age, self.per))

i = Inheritance(98.65, "rex", 23)
i.display()