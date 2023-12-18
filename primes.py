#!/usr/bin/env python3

from sympy import primerange
from sympy import factorint

def enumerate_primes(limit):
    primes = list(primerange(1, limit + 1))
    return primes

def example1():
    # Example usage:
    limit = 50
    prime_list = enumerate_primes(limit)
    print(f"Primes up to {limit}: {prime_list}")

def factorize_number(n):
    factors = factorint(n)
    return factors

def example2():
    # Example usage:
    n = 2 * 3 * 7
    factors = factorize_number(n)
    print(str(n) + ':', *factors)
