# file demo
# enter file name for creation
name=input("Enter file name:?")
file=open(name,"w")
msg=input("Enter the msg for the file")
file.write(msg)
file.flush()

# reading the file
reads=open("regis.txt","r").read()
print(reads)
file.close()
