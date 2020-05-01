s = [{input() for j in range(int(input()))} for i in range(int(input()))]
every, some = set.intersection(*s), set.union(*s)
print(len(every), *sorted(every), sep='\n')
print(len(some), *sorted(some), sep='\n')
