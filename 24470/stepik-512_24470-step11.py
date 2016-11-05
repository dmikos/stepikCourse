import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"\b(\w+)\1\b", line)

    if res:
        print(line)
        print(res.groups())
        print(res.group())
        print(res.group(0))
        print(res.group(1))

"""
Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:

blabla is a tandem repetition
123123 is good too
"""