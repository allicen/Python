import re
import sys
pattern = r"\ba+\b"

for line in sys.stdin:
    line = line.rstrip()
    out = re.sub(pattern, "argh", line, count=1, flags=re.IGNORECASE)
    print(out)
