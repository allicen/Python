import re
import sys
pattern = r"z.{3}z"

for line in sys.stdin:
    line = line.rstrip()
    out = re.findall(pattern, line)
    if len(out) > 0:
        print(line)
