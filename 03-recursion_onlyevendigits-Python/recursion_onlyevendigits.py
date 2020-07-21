# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def rec(l, res, count):
	if(count == len(l)):
		return res
	if(int(l[-1-count])%2 == 0):
		res += l[-1-count]
		return rec(l, res, count+1)
	else:
		return rec(l, res, count+1)
	


def fun_recursion_onlyevendigits(l):
	for i in range(0, len(l)):
		d = str(l[i])
		print(d[-1::-1])
		res = rec(d[-1::-1], "", 0)
		# print("res here:", int(res))
		if(res == ""):
			res = "0"
		l[i] = int(res)
	return l
	

# print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))