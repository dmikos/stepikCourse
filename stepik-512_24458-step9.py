#!/usr/bin/env python3

#https://stepik.org/lesson/%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D1%8B-24458/step/9?unit=6765
objects = [1, "wewe", 1, 2, '23', ('ss', 'dd', 3), {}]
res=set()

for obj in objects:
    res.add(type(obj))

print(res)
