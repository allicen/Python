count = int(input())
direction = {}
finish = {'x': 0, 'y': 0}

for i in range(count):
    line = input()
    arr = line.split()
    nameDirection = arr[0]
    countStep = arr[1]
    if nameDirection not in direction:
        direction[nameDirection] = int(countStep)
    else:
        direction[nameDirection] += int(countStep)

for i in direction:
    if i == 'север':
        finish['y'] += direction[i]
    elif i == 'юг':
        finish['y'] -= direction[i]
    elif i == 'восток':
        finish['x'] += direction[i]
    else:
        finish['x'] -= direction[i]

for i in finish:
    print(finish[i], end=' ')