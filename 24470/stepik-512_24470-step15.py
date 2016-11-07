# """
import sys
import re

line = "attraction"
# line = "buzzzz"
# res = re.search(r"(\w)\1+", line)
res = re.sub(r"(\w)\1+", r"\1", line)     # or res = re.sub(r"\b(\w)(\w)", "\\1", line)
print(res)
# print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))

"""
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(\w)\1+", r"\1", line))

"#""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:

attraction
buzzzz

Sample Output:

atraction
buz
"""