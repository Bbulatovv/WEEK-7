a = list(map(int, input().split()))
mySet = set()
for i in a:
    if i in mySet:
        print('YES')
    else:
        print('NO')
        mySet.add(i)
