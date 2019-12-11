import re
import sys
pattern = r"human"

for line in sys.stdin:
    line = line.rstrip()
    out = re.sub(pattern, "computer", line)
    print(out)
