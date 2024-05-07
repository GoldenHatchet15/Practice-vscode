#!/usr/bin/python3
import math

def test_pow():
    base = 2
    exponent = 3
    assert math.pow(base, exponent) == 8
    print("{}".format(math.pow(base, exponent)))

if __name__ == "__main__": 
    test_pow()

