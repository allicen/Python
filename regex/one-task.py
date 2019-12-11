import re
import sys
pattern = r"cat"

for line in sys.stdin:
    line = line.rstrip()
    out = re.findall(pattern, line)
    if len(out) >= 2:
        print(line)