#Demo for String function

name="regis charles"
newname=name[1]
print(newname ,end='')
for x in name:
    print(x)
if(name.islower()):
    print(name)
if(name.isupper()):
    print(name)
else:
    print(name.upper())
size=len(name)
s="""
hello my dear, how are you my jen..... hope you doing good.
  I'm here trying to find you
"""
no=s.count("you")
print(no)
print("size of the objecct is {0}".format(size))
emailid="regischarles7@gmail.com"
if(emailid.endswith("gmai.com")):
    print("its valid email")
else:
    print("Its not Valid email Id")
str1="Hello my name is regis"
#replace regis with rex
print(str1.replace("regis","rex"))
"""remember as string is immutable the operation replace will return new instance
of string hences the old string will remain the same
"""
print(str1)
#spillting method
str2="regis charles"
firstname,lastname=str2.split(" ")
print("firstname"+firstname+" lastname"+ lastname)
strpdemo="#####good morning####"
#stripping all # from left side using lstrip
print(strpdemo.lstrip('#'))
#stripping all # from right side using lstrip
print(strpdemo.rstrip('#'))
#stripping all # from strpdemo
print(strpdemo.strip('#'))
#swapping all upper case to lower case and vice versa
print(str2.swapcase())
print(str2.title())
