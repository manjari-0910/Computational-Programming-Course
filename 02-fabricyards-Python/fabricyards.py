# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
	yards = inches//36
	if(inches % 36 != 0):
    		yards+=1

	return yards

def fun_fabricexcess(inches):
	# your code goes here
	if(inches % 36 != 0):
    		return 36 - (inches% 36)
	else:
    		return 0

# print(fun_fabricexcess(72))
