import itertools


def primes():
    num = 2
    yield num
    while True:
        num += 1
        flag = 1
        for j in range(2, num-1):
            if num % j == 0:
                flag = 0
        if flag:
            yield num


if __name__ == "__main__":
    print(list(itertools.takewhile(lambda x: x <= 1000000, primes())))
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


