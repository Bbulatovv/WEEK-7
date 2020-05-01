myList = list(map(int, input().split()))
mySet = set(myList)
differentnum = 0
for i in mySet:
    differentnum += 1
print(differentnum)
