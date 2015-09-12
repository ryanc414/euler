# largest prime factor of 600851475143

N = 600851475143
prime_factors = []

# function to find factors of integer N
def find_factors(N):
    factors = []
    counter_factors = []
    prime = True

    sqrt_N = int(N ** 0.5)

    for i in range(2, sqrt_N):
        if (N % i) == 0:
            print "Factor found! %d" % i
            prime = False
            factors.append(i)
    
    for factor in factors:
        counter_factors.append(N / factor)

    factors = factors + counter_factors

    return factors

factors = find_factors(N)

# print factors

complete = False

while complete == False:
    complete = True

    for factor in factors:
        subfactors = find_factors(factor)

        if subfactors == []:
            print "Prime factor found! %d" % factor
            if factor not in prime_factors:
                prime_factors.append(factor)
            factors.remove(factor)
        else:
            complete = False
            factors.remove(factor)
            for n in subfactors:
                if n not in factors:
                    factors.append(n)

    print factors

print prime_factors
            
