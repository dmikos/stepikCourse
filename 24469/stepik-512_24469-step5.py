
# capital = 'London is the capital of Great Britain'
# template = '{} is the capital of {}'
# print(template.format("London", "Great Britain"))
# print('{} is the capital of {}'.format("London", "Great Britain"))
# print(template.format("Vaduz", "Liechtenstein"))
# print('{} is the capital of {}'.format("Vaduz", "Liechtenstein"))
# print(str.format.__doc__)

template = '{1} is the capital of {0}'
print(template.format("London", "Great Britain"))
print(template.format("Vaduz", "Liechtenstein"))
