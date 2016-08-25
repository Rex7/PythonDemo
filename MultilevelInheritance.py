"""
this is just a demo for inheritance (multi-level)
"""


class Human:
    """
    This is a simple demo
    """

    name = ""
    dob = ""

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display(self):
        pass


class Student(Human):
    roll_number = 0
    std = ""

    def __init__(self, roll, std, name, dob):
        self.roll_number = roll
        self.std = std
        super(Student, self).__init__(name, dob)

    def display(self):
        print("Name :{0} \nDate of Birth:{1} \nRoll Number:{2} \nStd:{3}".format(self.name, self.dob, self.roll_number,
                                                                                  self.std))


class Record(Student):
    english = 0
    marathi = 0
    math = 0
    history = 0
    geography = 0
    science = 0

    def __init__(self, english, marathi, math, history, geography, science, roll, std, name, dob):
        self.english = english
        self.marathi = marathi
        self.math = math
        self.history = history
        self.geography = geography
        self.science = science
        super(Record, self).__init__(roll, std, name, dob)

    def display(self):
        Student.display(self)
        print("English:{0}\nmath:{1}\nMarathi:{2}\nHistory:{3}\nGeography:{4}\nScience:{5}".format(self.english,
                                                                                                   self.math,
                                                                                                   self.marathi,
                                                                                                   self.history,
                                                                                                   self.geography,
                                                                                                   self.science))


r = Record(55, 65, 95, 45, 69, 96, 1, "12th", "Regis Charles", "18/8/1992")
r.display()
