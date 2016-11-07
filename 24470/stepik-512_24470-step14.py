# """
import sys
import re

line = "AaAaAaA AaAaAaA"
line = "There’ll be no more \"Aaaaaaaaaaaaaaa\""
print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))

"""
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))

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