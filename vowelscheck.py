# Demo for checking vowels in a string entered by users
count = 0
string = input("Enter your values")
for ltr in string:
    if(ltr in ['a','e','i','o','u','A','E','I','O','U']):
        count += 1
print(count)


