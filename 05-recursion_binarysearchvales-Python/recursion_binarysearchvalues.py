# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 

def recbinser(l, v, list1, low, high, mid):
	if(ord(l[mid]) == ord(v)):
		print("came here")
		list1.append((mid, l[mid]))
		return list1
	else:
		if(ord(v) > ord(l[mid])):
			low = mid+1
		else:
			high = mid-1
		if((low+high)//2 == mid):
			list1.append((mid, l[(low+high)//2]))
			return list1
		list1.append((mid, l[mid]))
		print(list1)
		return recbinser(l,v, list1, low, high, (low+high)//2)




def recursion_binarysearchvalues(L, v):
	# Your codes goes here
	list1 = []
	list1 = recbinser(L, v, list1, 0, len(L)-1, (0+len(L)-1)//2)
	return list1



print(recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'f'))