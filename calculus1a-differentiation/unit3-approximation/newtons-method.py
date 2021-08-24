from math import sin, cos, log # math.log is the natural logarithm. Dunno why it's not math.ln though.

def newtonsMethod(f, fPrime, x, guesses):
	'''
	Given an initial guess (x) and the amount of guesses to make (guesses), try to approximate the roots of the function f. fPrime is the derivative of f
	'''
	if (guesses == 0):
		return
	
	print(x)
	newtonsMethod(f, fPrime, x - f(x) / fPrime(x), guesses - 1)


f = lambda x: x**4 - sin(x**3) + 0.5**x + x - 5
fPrime = lambda x: 4 * x**3 - 3 * x**2 * cos(x**3) + log(0.5) * 0.5**x + 1

newtonsMethod(f, fPrime, 1, 10)
