myFile = open('input.txt', encoding='utf8')
myDictionary = {}
for line in myFile:
    words = line.strip().split()
    for word in words:
        myDictionary[word] = myDictionary.get(word, 0) + 1
print(sorted(myDictionary.items(), key=lambda x: (-x[1], x[0]))[0][0])
