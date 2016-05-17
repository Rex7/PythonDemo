#ListExample
n=int(input("Enter no of element in list"))
m=[]
for i in range(n):
    s=input("Enter your element in list")
    m.append(s)
    print("Entered element in list{0}".format(m))
print("Element in List{0}".format(m),end='')
def replace(index ,val ):
    m[index] = val
    print(m)
replace(len(m)-1,"rex")
