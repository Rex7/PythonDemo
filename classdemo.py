# program for simple student class creation
class Student:

    def __init__(self):
        self.name = ""
        self.roll_number = 0
        self.count = 0

    def read_data(self):
        self.name = input("Enter UserName:")
        self.roll_number = int(input("Enter Roll Number:"))

    def display(self):
        print("Name :{0} \n Roll Number:{1}".format(self.name, self.roll_number))
