#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python/Cython - prime number functions with speed test.

"""
from primes.pyprimes import primes as pyprimes
from primes.cyprimes import primes as cyprimes
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
        if kmax > KMAX:
            kmax = KMAX
    else:
        kmax = KMAX

    # Tests
    py_res = prime_test(pyprimes, kmax)
    cy_res = prime_test(cyprimes, kmax)
    
    # Result
    print('Each test printed {} prime numbers'.format(kmax))
    print('PYTHON: {} seconds'.format(py_res))
    print('CYTHON: {} seconds'.format(cy_res))

    if cy_res < py_res:
        print 'Cython was {} times faster'.format(int(round(py_res / cy_res)))
    elif py_res < cy_res:
        print 'Python was {} times faster'.format(int(round(cy_res / py_res)))


if __name__ == '__main__':
    main()
