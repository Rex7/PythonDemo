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
