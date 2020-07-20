# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def isprime(n):
	for i in range(2, n//2+1):
		if(n%i == 0):
			return False
	return True
    		



def fun_hasnoprimes(l):
	for i in l:
		for j in i:
			if(isprime(j)):
				return False
	return True

print(fun_hasnoprimes([[9,12],[8],[16,8]]))