import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"\\", line)
    if res:
        print(line)
