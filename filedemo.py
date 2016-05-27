# file demo
file=open("regis.txt","w")
msg=input("Enter the msg for the file")
file.write(msg)
file.flush()
read=open("regis.txt","r").read()
print(read)
