import re
import sys
pattern = r"\\"

for line in sys.stdin:
    line = line.rstrip()
    out = re.findall(pattern, line)
    if len(out) > 0:
        print(line)
