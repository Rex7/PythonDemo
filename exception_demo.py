a=int(input("Enter number for a"))
b=int(input("Enter number for b"))
try:
    c = b / a
    print("answer is : {0}".format(c))
except Exception as error:
    print("exception raised asshole {0}".format(error))
