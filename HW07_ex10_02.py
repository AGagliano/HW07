# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
#########################################################################

def capitalize_nested(l):
	'''Takes a list (okay if the list is of nested lists) and returns
	a new listed (still nested, if applicable) with all the strings
	capitalized. 

	Function uses list comprehension and recursively calls the function
	again when an element in the list is still a list (i.e. a nested list).
	When the function reaches a string, it capitalizes it.
	'''
	l_cap = [capitalize_nested(word) if type(word) is list else str.capitalize(word) for word in l]
	return l_cap


#########################################################################

def main():
	pass

if __name__ == "__main__":
	main()