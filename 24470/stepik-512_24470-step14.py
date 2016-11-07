# """
import sys
import re

line = "this is a text"
line = "\"this' !is. ?n1ce,"
# res = re.findall(r"\b(\w)(\w)", line)
res = re.sub(r"\b(\w)(\w)", "\\2\\1", line)     # or res = re.sub(r"\b(\w)(\w)", r"\2\1", line)
print(res)
# print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))

"""
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b(\w)(\w)", r"\2\1", line))

#""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w﻿.

Sample Input:

this is a text
"this' !is. ?n1ce,

Sample Output:

htis si a etxt
"htis' !si. ?1nce,
"""