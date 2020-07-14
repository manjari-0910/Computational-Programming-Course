# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	list1 = []
	if(abs(n) == n):
			while(n > 0):
					list1.append(str(n%10))
					n = n//10
			if(k >= len(list1)):
    				list1.append(str(d))
			else:
					list1[k] = str(d)
			list1.reverse()
			new = "".join(list1)
			return int(new)
	else:
		n = abs(n)
		while(n > 0):
			list1.append(str(n%10))
			n = n//10
		if(k >= len(list1)):
    			list1.append(str(d))
		else:
				list1[k] = str(d)
		list1.reverse()
		new = "".join(list1)
		new = "-"+ new
		return int(new)

print(fun_set_kth_digit(-468, 3, 1))