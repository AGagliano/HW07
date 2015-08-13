# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
#########################################################################


def nested_sum(l):
	'''Takes a nested list of integers and sum up all the elements from
	all the nested lists using list comprehension. The function returns the sum.
	'''
	l_flatter = [nested_sum(item) if type(item) is list else item for item in l]
	return sum(l_flatter)

# Is it possible to eliminate the total counter when using a for loop
# since total is not necessary when using list comprehension? 
# Or is that a benefit of list comprehension?
def nested_sum_alternate(l, total = 0):
	'''Takes a nested list of integers and sum up all the elements from
	all the nested lists using a for loop. The function returns the sum.
	'''
	for item in l:
		if type(item) is list:
			total = nested_sum(item, total)
		else: 
			total = total + item
	return total

#########################################################################

def main():
	pass

if __name__ == "__main__":
	main()