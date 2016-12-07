"""This module defines functions that implement mathematical series."""

def fibonacci(n):
	"""Returns the nth number of the Fibonacci sequence (starting with 0, 1)"""
	first = 0
	second = 1
	if n == 1:
	    return first
	elif n == 2:
	    return second
	else:
	    for num in range(n - 2):
	        third = first + second
	        first = second
	        second = third
	    return second


def lucas(n):
	"""Returns the nth number of the Lucas sequence (starting with 2, 1)"""
	first = 2
	second = 1
	if n == 1:
	    return first
	elif n == 2:
	    return second
	else:
	    for num in range(n - 2):
	        third = first + second
	        first = second
	        second = third
	    return second


def sum_series(n, first=0, second=1):
	"""Returns the nth number of the Fibonacci sequence, or a different sequence starting with the parameters given"""
	if n <= 1:
	    return first
	return sum_series(n - 1, second, second + first)

if __name__ == "__main__":
	print()
	print(__doc__)
	print("...")
	print()
	print("fibonacci(n):")
	print()
	print("    " + fibonacci.__doc__)
	print()
	print("lucas(n):")
	print()
	print("    " + lucas.__doc__)
	print()
	print("sum_series(n):")
	print()
	print("    " + sum_series.__doc__)
	print()