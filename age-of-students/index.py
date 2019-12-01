import codecs

data = {}
result = ''

with codecs.open('input.txt', 'r', 'utf_8_sig') as inf:
    for line in inf:
        line = line.strip()
        arr = line.split('\t')
        numberClass = 0

        for i in range(len(arr)):
            if i == 0:
                if int(arr[i]) not in data:
                    data[int(arr[i])] = {
                        'sum': 0,
                        'count': 0
                    }
                numberClass = int(arr[i])
            if i == 2:
                data[numberClass]['sum'] += int(arr[i])
                data[numberClass]['count'] += 1

for i in range(1, 12):
    result += str(i)
    result += '\t'
    if i in data:
        result += str(data[i]['sum']/data[i]['count'])
    else:
        result += '-'
    result += '\n'

print(result)