import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self):
        print("tess")
        # super(LoggableList, self).append()


if __name__ == "__main__":
    x = LoggableList()
    # print(x)
    x = []
    print(x)
    x.append("dd")
    x.append("cfc")
    print(x)
