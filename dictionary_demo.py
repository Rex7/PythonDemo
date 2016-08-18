"""
Dictionary is a data structure which is of key - value pair
"""
dic={1:"regis",2:"charles"}
tup=()
lis=[]
print("Printing Dictionary ")

def dictionary(data):
    if type(data) is dict:
        for key,val in dic.items():
            print("Key : {0} -> Value :{1} ".format(key,val))
    else:
        print("its not of type dict")
dictionary(dic)
# below function calls will give different output
dictionary(tup)
dictionary(lis)