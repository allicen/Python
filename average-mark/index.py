import codecs

data = []
averageMarkStudent = []
averageMarkSubjectSum = [0, 0, 0]
countSubject = 3
countStudents = 0
result = ''

with codecs.open('input.txt', 'r', 'utf_8_sig') as inf:
    for line in inf:
        line = line.strip()
        data.append(line.split(';'))
        countStudents += 1

for i in range(len(data)):
    marks = 0
    for j in range(len(data[i])):
        if j != 0:
            marks += int(data[i][j])
            averageMarkSubjectSum[j-1] += int(data[i][j])
    averageMarkStudent.append(marks/countSubject)

for i in averageMarkStudent:
    result += str(i)
    result += '\n'

for i in averageMarkSubjectSum:
    result += str(i/countStudents)
    result += ' '

with open('output.txt', 'w') as ouf:
    ouf.write(result)