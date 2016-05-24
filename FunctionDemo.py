#Function type and way it works
def printmyname(name,age):
    print("name of the person is:",name,age)
printmyname(age=22,name="regis")
#function with defualt argument
def value(user="admin"):
    print("Welcome user:",user)
#passsing no arguments gives the default value set
value()
#if argument is passed then the default value is overriden
value("Rex")
#function which returns values
def add(a,b):
    return a+b
ans=add(10,69)
print(ans)
def anynumber(*av):
    for i in av:
        print(i)
#function if doesnt return anything explicitly then it will return None
def ret():
    pass
s=ret()
print(s)
#variable argument
ar=(18,22)
anynumber(ar)
#calculator
def cal(a,b,flag):
    if(flag==0):
        return a+b
    elif(flag==1):
        return a-b
    elif(flag==2):
        return a*b
    elif(flag==3):
        return a/b
    else:
        return
print("addition of 20 and 10 :",cal(20,10,0))
print("sub of 20 and 10 :",cal(20,10,1))
print("multiplication of 20 and 10 :",cal(20,10,2))
print("division of 20 and 10 :",int(cal(20,10,3)))