s = input()
t = input()
count = 0
pos = 0
while pos < len(s):
    if s.startswith(t, pos):
        count += 1
    pos += 1

print(count)
