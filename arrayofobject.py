"""
This is a demo for array of objects
"""
class emp:
    def __init__(self):
        e_name = ""
        e_sal = 0.0
        e_id = 0
    def read_emp(self):
        self.e_name=str(input("Enter Name:"))
        self.e_id=int(input("Enter Employee Id:"))
        self.e_sal=float(input("Enter Salary of Employee:"))
    def display_emp_record (self):
        print("Printing Employee Detals ")
        print("Employee Id:{0}\nEmployee Name:{1}\nSalary:{2}".format(self.e_id,self.e_name,self.e_sal))

list_data=[]
s=0
no=int(input("Enter the number of object to create:"))
for i in range(no):
    m=emp()
    list_data.append(m)
for i in range(no):
    list_data[i].read_emp()
for i in range(no):
    list_data[i].display_emp_record()








