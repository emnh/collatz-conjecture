#!/usr/bin/env python3

from collatz import collatz_cycle
from collatz import get_first_n_cycles
from collatz import list_to_latex
from collatz import list_first_20
from sympy import primerange
from sympy import factorint

#list_first_20()

for n in range(1, 40+1):
    factors = factorint(n)
    cycle = list(collatz_cycle(n))
    has3 = 3 in factors
    has2 = 2 in factors
    print(n, has2, has3, factors, cycle)
