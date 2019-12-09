with open("input.txt") as pw:
    line = pw.read().splitlines()

f = open("output.txt", "w")

for i in reversed(line):
    f.write(str(i) + "\n")
