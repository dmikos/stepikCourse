import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, var):
        super(LoggableList, self).append(var)
        super(LoggableList, self).log(var)


if __name__ == "__main__":
    x = LoggableList()
    print(x)
    x.append("ss")
    print(x)
    x.append("dd")
    x.append("cfc")
    print(x)
