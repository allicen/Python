s = input()
a = input()
b = input()
count = 0

while s.find(a) != -1:
    if count > 1000:
        break
    else:
        s = s.replace(a, b)
        count += 1

result = 'Impossible' if count > 1000 else count

print(result)