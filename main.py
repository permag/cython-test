#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python vs. Cython - prime function with speed test.

"""
import primes as cyprimes
import pyprimes
import time
import sys

KMAX = 5000  # max prime numbers


def prime_test(f, kmax):
    start = time.time()
    print(f(kmax))
    stop = time.time()
    return stop - start


def main():
    if len(sys.argv) > 1:
        kmax = int(sys.argv[1])
    else:
        kmax = KMAX

    # Tests
    py_res = prime_test(pyprimes.primes, kmax)
    cy_res = prime_test(cyprimes.primes, kmax)
    
    # Result
    print('Each test printed {0} prime numbers.'.format(kmax))
    print('PYTHON: {} seconds'.format(py_res))
    print('CYTHON: {} seconds'.format(cy_res))


if __name__ == '__main__':
    main()
