d = int(input())
words = set()
text = []
result = set()

for i in range(d):
    new = input()
    words.add(new.lower())

lines = int(input())

for i in range(lines):
    line = input().split()
    text.append(line)

for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j].lower() not in words:
            result.add(text[i][j].lower())

for i in result:
    print(i)