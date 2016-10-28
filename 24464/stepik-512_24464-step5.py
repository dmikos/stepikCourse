import itertools


def primes():
    num = 2
    if 1:
        yield num
    num += 1


if __name__ == "__main__":
    print(list(itertools.takewhile(lambda x: x <= 31, primes())))
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


