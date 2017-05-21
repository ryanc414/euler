#!/usr/bin/env python3
"""P6: Square of sum minus sum of squares.
(1 + 2 + ...)^2 - 1^2 + 2^2 + ..."""

N = 100


def main():
    result = 0

    for i in range(1, N):
        for j in range(i+1, N+1):
            result += i * j

    result *= 2
    
    return result


if __name__ == '__main__':
    print((main()))

