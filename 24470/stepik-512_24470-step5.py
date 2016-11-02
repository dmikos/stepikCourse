import re
"""
pattern = r"(test)*"
string = "test"
match = re.match(pattern, string)
print(match)

pattern = r"(test)*"
string = "testtest"
match = re.match(pattern, string)
print(match)

pattern = r"(test|text)*"
string = "testtest"
match = re.match(pattern, string)
print(match)
string = "testtext"
match = re.match(pattern, string)
print(match)

pattern = r"abc|(test|text)*"
string = "testtext"
match = re.match(pattern, string)
print(match)

pattern = r"abc|(test|text)*"
string = "abc"
match = re.match(pattern, string)
print(match)

pattern = r"((abc)|(test|text)*)"
string = "abc"
match = re.match(pattern, string)
print(match)
print(match.groups())

pattern = r"((abc)|(test|text)*)"
string = "testtext"
match = re.match(pattern, string)
print(match)
print(match.groups())

pattern = r"((abc)|(test|text)*)"
string = "testtexttest"
match = re.match(pattern, string)
print(match)
print(match.groups())
"""
pattern = r"Hello (abc|test)"
string = "Hello abc"
match = re.match(pattern, string)
print(match)
print(match.group())
print(match.group(0))
print(match.group(1))
