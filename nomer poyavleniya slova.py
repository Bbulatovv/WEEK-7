n = dict()
myFile = open('input.txt', 'r', decoding='utf8')
for line in myFile:
    for word in line.strip().split():
        n[word] = n.get(word, -1) + 1
        print(n[word], end=' ')
