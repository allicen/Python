a = input()
b = input()
c = input()
d = input()

shifr = {}
unShifr = {}
result = ''

for i in range(len(a)):
    shifr[a[i]] = b[i]
    unShifr[b[i]] = a[i]

for i in range(len(c)):
    result += shifr[c[i]]

result += '\n'

for i in range(len(d)):
    result += unShifr[d[i]]

print(result)