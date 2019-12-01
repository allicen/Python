n = int(input())

matches = []
win, lose, draw = 3, 0, 1
commands = {}
result = ''

for i in range(n):
    line = input().split(';')
    matches.append(line)

for i in range(len(matches)):
    points = []
    for j in range(len(matches[i])):
        if not matches[i][j].isdigit():
            if matches[i][j] not in commands:
                commands[matches[i][j]] = {
                    'playCount': 1,
                    'winCount': 0,
                    'drawCount': 0,
                    'loseCount': 0
                }
            else:
                commands[matches[i][j]]['playCount'] += 1
        else:
            points.append(int(matches[i][j]))
    oneCommandName = matches[i][0]
    twoCommandName = matches[i][2]
    oneCommandPoint = points[0]
    twoCommandPoint = points[1]
    if oneCommandPoint > twoCommandPoint:
        commands[oneCommandName]['winCount'] += 1
        commands[twoCommandName]['loseCount'] += 1
    elif oneCommandPoint < twoCommandPoint:
        commands[twoCommandName]['winCount'] += 1
        commands[oneCommandName]['loseCount'] += 1
    else:
        commands[oneCommandName]['drawCount'] += 1
        commands[twoCommandName]['drawCount'] += 1

for i in commands:
    result += i
    result += ': '
    total = 0
    for j in commands[i]:
        if j == 'playCount':
            result += str(commands[i][j])
            result += ' '
        elif j == 'winCount':
            result += str(commands[i][j])
            result += ' '
            total += commands[i][j] * win
        elif j == 'drawCount':
            result += str(commands[i][j])
            result += ' '
            total += commands[i][j] * draw
        else:
            result += str(commands[i][j])
            result += ' '
    result += str(total)
    result += '\n'

print(result)