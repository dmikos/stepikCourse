import re

line = input()
while line:
    res = re.findall(r"\bcat\b", line)
    if res and res[0] == 'cat':
        print(line)
    line = input()

"""
print(re.findall(r"\bcat\b", "catapult and cat"))
print(re.findall(r"\bcat\b", "catcat"))
print(re.findall(r"\bcat\b", "concat"))
print(re.findall(r"\bcat\b", "Cat"))
print(re.findall(r"\bcat\b", "\"cat\""))
print(re.findall(r"\bcat\b", "!cat\?"))


Вам дана последовательность строк. Выведите строки, содержащие "cat" в качестве слова.
Примечание: Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.

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