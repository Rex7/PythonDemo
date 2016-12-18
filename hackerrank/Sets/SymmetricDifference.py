"""
Given  sets of integers, m and n, print their symmetric difference in ascending order.
 The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
"""
m = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
c = sorted(a.symmetric_difference(b))
for element in c:
    print(element)
