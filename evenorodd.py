"""
program for printing even or odd from 1 to 50
"""
def number_check(number):
        if number%2==0:
            print("number is even :{0}".format(number))
        else:
            print("number is odd {0}".format(number))
for i in range(50):
    number_check(i)

