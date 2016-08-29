"""
This is a simple demo for implementing queue using deque coz it increases efficient
"""

import collections

queue = collections.deque()
print("Simple Queue Using Deque")
no = int(input("Enter Number Of Element In Queue :"))
for i in range(no):
    item = input("Enter Element:")
    queue.append(item)
print(queue)