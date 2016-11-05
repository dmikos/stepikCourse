import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"\bcat\b", line)
    if res:
        print(line)


"""
Sample Input:
    cat
    catapult and cat
    catcat
    concat
    Cat
    "cat"
    !cat?
Sample Output:
    cat
    catapult and cat
    "cat"
    !cat?
"""