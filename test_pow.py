#!/usr/bin/python3
import math

def test_pow():
    base = 3
    exponent = 3
    assert math.pow(base, exponent) == 8
    print("{}".format(math.pow(base, exponent)))

# Uncomment the following line if you want to call the test function without using pytest
test_pow()
