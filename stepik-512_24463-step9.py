class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, var):
        if var > 0:
            super(PositiveList, self).append(var)
        else:
            raise NonPositiveError()

x = PositiveList()
print(x)
x.append(2)
print(x)