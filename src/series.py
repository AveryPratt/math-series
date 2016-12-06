def fibonacci(n):
    start = 0
    second = 1
    if n == 1:
        return start
    elif n == 2:
        return second
    else:
        for num in range(n - 2):
            third = start + second
            start = second
            second = third
        return second


def lucas(n, m=2, o=1):
    if n <= 1:
        return m
    return lucas(n - 1, o, o + m)


def sum_series(n, m=0, o=1):
    if n <= 1:
        return m
    return sum_series(n - 1, o, o + m)
