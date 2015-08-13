# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#########################################################################

def is_sorted(l):
	'''Function takes a list and returns True if the list is sorted 
	in ascending order and False otherwise. 

	Function assumes that the elements of the list can be compared 
	with the relational operators <, >, etc. (e.g. given list 
	shouldn't mix capitals and lower cases).
	Ex: [1,2,2] returns True
	Ex: ['b','a'] returns False
	'''
	#All command returns True if the condition is always True 
	#throughout the for loop.
	return all(l[i] > l[i-1] for i in range(1, len(l)))

#########################################################################
def main():
	pass

if __name__ == "__main__":
	main()