# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	val = int(n)
	rem = n/float(val)
	if(rem == 0):
		if(val%2 == 0):
			print(here)
			return val-1
		else:
			print(here)
			return val
	else:
		if(val%2 == 0):
				return val+1
		else:
				return val


print(fun_nearestodd(12.0))