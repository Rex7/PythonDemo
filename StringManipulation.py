#Demo for String function

name="regis charles"
newname=name[1]
print(newname ,end='')
for x in name:
    print(x)

capital=name.capitalize()
lowercase=name.lower()
uppercase=name.upper()
size=len(name)
print(size)
#replace e with x
changed=name.replace('e','x',3)
print("Changed name"+changed)
print("name in capital :",capital,"name in upper case:",uppercase,"name in lower case",lowercase)
print(name)