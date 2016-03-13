""" 
Author = Cedric Kim
A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	if not exists(file_name) or reset:		##if the file does not exist, or reset is true
		counter_string = 'counter = 0'		##make a string with counter 0
		pickle.dump(counter_string, open(file_name, 'w'))	##dump the data into a the file 
	counter_string = pickle.load(open(file_name, 'r+'))		##open the file in r+
	counter_number = int(counter_string.lstrip('counter ='))	##find the value of the counter
	updated_counter_string = 'counter = ' + str(counter_number+1)	##update the counter
	pickle.dump(updated_counter_string, open(file_name, 'r+'))		##dump the new value in the file
	return counter_number + 1										##returns the value

if __name__ == '__main__':
	import pickle
	import doctest
	doctest.testmod()
	print "new value is " + str(update_counter('test.txt'))