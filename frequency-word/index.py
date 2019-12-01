string = []
sameWord = {}

with open('input.txt') as data:
    for line in data:
        line = line.strip().split()
        string.append(line)

for i in range(len(string)):
    for j in range(len(string[i])):
        if string[i][j].lower() not in sameWord:
            sameWord[string[i][j].lower()] = 1
        else:
            sameWord[string[i][j].lower()] += 1

maximum = sameWord[string[0][0].lower()]
values = []

for i in sameWord:
    if maximum < sameWord[i]:
        maximum = sameWord[i]
        values.clear()
        values.append(i)
    elif maximum == sameWord[i]:
        values.append(i)

values.sort()

result = values[0] + '\t' + str(maximum)

with open('output.txt', 'w') as ouf:
    ouf.write(result)