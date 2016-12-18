def largest(li):
    return max(li)


n = input()
no = input()
lis = no.split()
lis = [int(i) for i in lis]
lis.sort()
index = (lis.index(largest(lis))) - 1
print(lis[index])