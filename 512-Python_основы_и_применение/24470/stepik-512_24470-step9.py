import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"z...z", line)
    if res:
        print(line)


"""
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
    zabcz
    zzxzz
"""