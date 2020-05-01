n = int(input())
myDictionary = {}
for i in range(n):
    first, second = input().split()
    myDictionary[first] = second
    myDictionary[second] = first
print(myDictionary[input()])
