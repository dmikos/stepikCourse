#!/usr/bin/env python3

# https://stepik.org/lesson/%D0%9D%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2-24462/step/8?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6768
version__ = "$Revision: 201610181516 $"
# $Source$


class ExtendedStack(list):
    def sum(self):
        # операция сложения
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)

    def sub(self):
        # операция вычитания
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)

    def mul(self):
        # операция умножения
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)

    def div(self):
        # операция целочисленного деления
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)


if __name__ == "__main__":
    x = ExtendedStack([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(x)
    # x.sum()
    # print(x)
    # x.sub()
    # print(x)
    # x.mul()
    # print(x)
    x.div()
    print(x)
