#!/usr/bin/env python3

#https://stepik.org/lesson/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B-24461/step/8?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6767

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.count + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.count += v

