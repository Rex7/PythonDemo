
"""
Stack Demo Using List
"""


def stack():

    __stack = []
    choice = 0
    while choice != 3:
        print("\n1:Push\n2:Pop\n3:Exit")
        no = int(input("Enter Your Choice :"))
        if no == 1:
            item = input("Enter Your Data To Push:")
            __stack.append(item)
            print(__stack)
        elif no == 2:
            __stack.pop()
            print(__stack)
        elif no == 3:
            break
        else:
            print("Wrong Number")

stack()


