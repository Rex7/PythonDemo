# program for simple student class creation
class student:
    def __init__(self):
        s_name = ""
        s_roll=0
    def read_data(self):
        self.s_name=str(input("Enter Student Name:"))
        self.s_roll= int(input("Enter Roll Number"))
    def display(self):
        print("Student Name : {0} and Roll Number : {1}".format(self.s_name,self.s_roll))
s1=student()
s1.read_data()
s1.display()