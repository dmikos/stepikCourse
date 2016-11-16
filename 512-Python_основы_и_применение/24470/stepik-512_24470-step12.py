import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"human", "computer", line))

"""
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
"""
