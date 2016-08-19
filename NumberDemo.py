# This is just a demo
integer=0
floating_point=0.0
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


new_list=[]
number_search(9,lis)
