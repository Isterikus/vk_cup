from math import sqrt
from itertools import count, islice


def isPrime(n):
	if n < 2: return False
	for number in islice(count(2), int(sqrt(n) - 1)):
		if not n % number:
			return False
	return True


x2 = int(input())


def primes1(n):
	""" Returns  a list of primes < n """
	sieve = [True] * (n / 2)
	for i in range(3, int(n ** 0.5) + 1, 2):
		if sieve[i / 2]:
			sieve[i * i / 2::i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
	return [2] + [2 * i + 1 for i in range(1, n / 2) if sieve[i]]


pr2 = primes1(x2 // 2)

