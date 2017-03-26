# special pythagorean triplet
# find abc for a^2 + b^2 = c^2 and a + b + c = 1000, a < b < c

from sys import exit


class CannotFindCException(Exception):
	"""Exception raised when no valid c is found"""
	pass

def get_c(a, b):
	"""return c for a^2 + b^2 = c^2"""
	for c in range(1, N + 1):
		if c * c == a * a + b * b:
			return c
	else:
		raise CannotFindCException("a = {0}, b = {1}".format(a, b))

def print_results(a, b, c):
	"""print a, b, c in readable format"""
	print "a = {0}, b = {1}, c = {2}".format(a, b, c)			
	print "Product abc = {0}".format(a * b * c)
	
def find_special_pythagorean_triplet(N):
	"""main function"""
	for a in range(1, N + 1):
		for b in range(a + 1, N + 1):
			try:
				c = get_c(a, b)
				if a + b + c == N:
					print_results(a, b, c)
					exit(0)
			except CannotFindCException:
				pass
	else:
		print "FAIL"
		
if __name__ == '__main__':
	N = 1000
	find_special_pythagorean_triplet(N)
	# if we get this far then we haven't found anything
	exit(2)