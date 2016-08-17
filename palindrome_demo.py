print("Palindrome Program ")
s=str(input("Enter The String:"))
size=len(s)-1
flag=False
for x in range(0,len(s)):
   if size==0:
       print("end of string s")
       break
   else:
       if s[x]==s[size]:
           print("s[x]= {} and s[size]={}".format(s[x],s[size]))
           flag=True
           print(flag)
       else:
           flag=False
           break

   size -=1
if flag==True:
    print("Its a Palindrome ")
else:
    print("Its not a Palindrome ")