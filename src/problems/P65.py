#!/usr/bin/env python

def find_numerator(x, n):
    a = [x[n]]
    b = [1]

    for i in range(1, n + 1):
        b.append(a[i - 1])
        a.append((x[n - i ] * a[i - 1]) + b[i - 1])

    return a[-1]


def fill_x(n):
    x = [2]

    for i in range(n):
        if i % 3 == 1:
            x.append(2 * (i // 3 + 1))
        else:
            x.append(1)

    return x

def fill_x_2(n):
    x = [1]

    for i in range(n):
        x.append(2)

    return x

def main():
    n = 99

    x = fill_x(n)

    print("{}th approx to e's digit sum = {}".format(
        n, sum(int(d) for d in str(find_numerator(x, n)))))


if __name__ == '__main__':
    main()

