"""

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def tempo(self):
        print("tte")


# if __name__ == "__main__":
    # pass
"""
class NonPositiveError(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise NonPositiveError(name + " is inappropriate name")

print(greet("Anton"))
print(greet("anton"))
