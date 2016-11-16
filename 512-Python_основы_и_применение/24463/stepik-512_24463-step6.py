def foo(var1, var2):
    var1 / var2

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


if __name__ == "__main__":
    pass