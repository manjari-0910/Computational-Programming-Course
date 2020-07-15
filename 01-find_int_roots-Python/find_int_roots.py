# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

from math import sqrt
def fun_find_int_roots(a, b, c):
	sol1 = sqrt(b**2 - (4*a*c))
	den = 2*a
	num1 = -b + sol1
	num2 = -b - sol1

	root1 = num1/den
	root2 = num2/den

	return root1, root2


print(fun_find_int_roots(1, -6, 8))	


