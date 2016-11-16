import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

pattern = r"abc"
string = "abcdd"
match_object = re.match(pattern, string)
print(match_object)

pattern = r"abc"
string = "dabcdd"
match_object = re.match(pattern, string)
print(match_object)

pattern = r"abc"
string = "dabcdd"
match_object = re.search(pattern, string)
print(match_object)

print("MetaSymbols")

# [] -- можно указать множество подходящих символов
pattern = r"a[abc]c"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)

pattern = r"a[abc]c"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)

pattern = r"a[abc]c"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)

print("Next")

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
