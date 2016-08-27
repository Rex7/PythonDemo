"""
Queue Demo using list
"""


def queue():

    __queue = []
    choice = 0
    while choice != 3:
        print("\n1:Push\n2:Pop\n3:Exit")
        no = int(input("Enter Your Choice :"))
        if no == 1:
            item = input("Enter Your Data To Push:")
            __queue.append(item)
            print(__queue)
        elif no == 2:
            if len(__queue) == 0:
                print("List Is Empty :{0}".format(__queue))
            else:
                item = __queue.pop(0)
                print("Item popped out is :{0}".format(item))
                print(__queue)
        elif no == 3:
            break
        else:
            print("Wrong Number")

queue()