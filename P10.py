# sum of all primes below N
from P7 import is_prime

N = int(2e6)

def main(N):
	sum = 0
	
	for i in range(1, N):
		if is_prime(i):
			sum += i
			
	print "Sum of primes less than {0} is {1}".format(N, sum)
	
if __name__ == '__main__':
	main(N)