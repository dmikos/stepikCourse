#!/usr/bin/env python3

def func():
    a = 'test func'
    print("func = ", a)

a = 'test global'
print("1 = ", a)

func()
print("2 = ", a)

if __name__ == "__main__":
    pass