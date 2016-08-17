# program for printing prime number from 1 to 100
def n(no):
    flag=0
    for x in range(2,100):
        if no%x==0:
            flag=flag+1
    if(flag==1):
        print("it is prime number {}".format(no))
for i in range(1,100):
    n(i)
