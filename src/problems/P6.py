#!/usr/bin/env python
# square of sum minus sum of squares
# (1 + 2 + ...)^2 - 1^2 + 2^2 + ...

N = 100
sum = 0

for i in range(1, N):
    for j in range(i+1, N+1):
        sum += i * j

sum *= 2

print sum
