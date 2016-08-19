# This is just a demo
integer=int(input("Enter Number One"))
floating_point=float(input("Enter Number two"))
add=integer+floating_point
print("addition of a floating point and integer gives out {0}".format(add))

# simple list demo for searching a integer  given number in the list

lis=[12,35,236,78,9]
print("Printing Elements in reverse order")
for x in range(len(lis)-1,-1,-1):
    print(lis[x])
def number_search( data , list_ ):
    if data is  None:
        print("bitch there is nothing ")
    else:
        if data in list_:
            print("Number found ")
        else:
            print("Number not found")
number_search(9,lis)
