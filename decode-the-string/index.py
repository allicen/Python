string = ''
result = ''

with open('input.txt') as data:
    for line in data:
        string = line.strip()

letter = ''
number = ''

for i in range(len(string)):
    if string[i].isalpha():
        string[i].isalpha()
        n = 0
        if number != '':
            n = int(number)
        for j in range(n):
            result += letter
        letter = string[i]
        number = ''
    else:
        number += string[i]

# Последний символ
for j in range(int(number)):
    result += letter

with open('output.txt', 'w') as ouf:
    ouf.write(result)

print(result)