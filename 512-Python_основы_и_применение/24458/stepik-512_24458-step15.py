#!/usr/bin/env python3

#https://stepik.org/lesson/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B8-%D1%81%D1%82%D0%B5%D0%BA-%D0%B2%D1%8B%D0%B7%D0%BE%D0%B2%D0%BE%D0%B2-24459/step/15?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6764

def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    elif k <= n:
        return C(n-1, k) + C(n-1, k-1)


#n = int(input())
#k = int(input())
n, k = map(int, input().split())

print(C(n, k))
