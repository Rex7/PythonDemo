class Person:
    name = " "
    dob = " "
    
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display(self):
        print("am in Person class")

class Employee(Person):

    emp_id = 0
    emp_sal = 0.0

    def __init__(self, emp_id, emp_sal, name, dob):
        self.emp_id = emp_id
        self.emp_sal = emp_sal
        super(Employee, self).__init__(name, dob)

    def display(self):
        print("Employee")

def whois(Person):
    p = Person
    p.display()

Emp = Employee (1, 6955.36, "regis charles", "18.8.1992")
whois(Emp)
Pers = Person("Regis Charles", "18.8.92" )

