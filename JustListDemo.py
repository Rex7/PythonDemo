#ListExample
no_of_element = int(input("Enter no of element in list"))
# assigning an empty list
old_list = []
for i in range(no_of_element):
    s = input("Enter your element in list")
    old_list.append(s)
    print("Entered element in list{0}".format(old_list))
print("Element in List{0}".format(old_list), end='')
def replace(index ,val ):
    old_list[index] = val
    print(old_list)
replace(len(old_list)-1,"rex")
""" assigning old list to new list in which if new list is changed then
the values of old list also changes and vice versa"""
new_list=old_list
new_list.append("babe")
old_list.append("last")
print(new_list)
print(old_list)