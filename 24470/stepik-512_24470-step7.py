import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'cat', line)) >= 2:
        print(line)

    # process line

"""
Sample Input:
    catcat
    cat and cat
    catac
    cat
    ccaatt
Sample Output:
    catcat
    cat and cat
"""