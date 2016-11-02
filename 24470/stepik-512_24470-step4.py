import re

pattern = r"ab{2,4}a"
string = "aa, aba, abba, abbba, abbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# "жадный", максимальный поиск
pattern = r"a[ab]+a"
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))

# "не жадный", наименьший поиск
pattern = r"a[ab]+?a"
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))
