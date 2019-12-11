import re
import sys
pattern = r"\b(\w)(\w)"

for line in sys.stdin:
    line = line.rstrip()
    outLine = re.sub(pattern, r"\2\1", line)
    print(outLine)

