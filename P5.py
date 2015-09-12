# smalest integer divisible by all integers in range 0-20
n = 20
n_max = int(1.0e7)
i = 3

while True:
    # print "n = %d" % n
    while n % i == 0:
        i += 1
    if i >= 20:
        break
    else:
        i = 1
        n += 20

print n
