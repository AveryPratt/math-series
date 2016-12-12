"""This module defines functions that implement mathematical series."""

def fibonacci(n):
	"""Returns the nth number of the Fibonacci sequence (starting with 0, 1)"""
	first = 0
	second = 1
	if n == 1:
		return first
	elif n == 2:
		return second
	for num in range(n - 2):
		second = second + first
		first = second - first
	return second


def lucas(n):
	"""Returns the nth number of the Lucas sequence (starting with 2, 1)"""
	first = 2
	second = 1
	if n == 1:
	    return first
	elif n == 2:
	    return second
	for num in range(n - 2):
		second = second + first
		first = second - first
	return second


def sum_series(n, first=0, second=1):
	"""Returns the nth number of the Fibonacci sequence, or a different sequence starting with the parameters given"""
	if n <= 1:
	    return first
	return sum_series(n - 1, second, second + first)

if __name__ == "__main__":
	output = """

""" + __doc__ + """
...

fibonacci(n):

    """ + fibonacci.__doc__ + """

lucas(n):

    """ + lucas.__doc__ + """

sum_series(n):

    """ + sum_series.__doc__

	print(output)