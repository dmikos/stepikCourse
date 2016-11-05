import sys
import re

res = re.search(r"\b(\w+)\1\b", "blabla is a tandem repetition")
print(res)
res = re.search(r"\b(\w+)\1\b", "is a tandem blabla repetition")
print(res)
res = re.search(r"\b(\w+)\1\b", "123123 is good too")
print(res)
res = re.search(r"\b(\w+)\1\b", "go go")
print(res)
res = re.search(r"\b(\w+)\1\b", "aaa")
print(res)



"""for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"\\", line)
    if res:
        print(line)

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:

blabla is a tandem repetition
123123 is good too
"""