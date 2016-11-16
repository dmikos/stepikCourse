
# s = "abababa"
# t = "aba"
# Output = 3

# s = "aaaaa"
# t = "a"
# Output = 5

# print(len(s))
# print(len(t))

s = str(input())
t = str(input())

count = 0
for i in range(len(s)-len(t)+1):
    if s[i:].startswith(t):
        count += 1
print(count)
