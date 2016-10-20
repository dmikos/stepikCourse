import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def tempo(self):
        print("tte")


if __name__ == "__main__":
    x = LoggableList()
    print(x)
    x.tempo()
