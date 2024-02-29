"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    # base case
    if x.decimal_val < 10 or y.decimal_val < 10:
        return x.decimal_val * y.decimal_val 
    
    # calculate the size of numbers
    n = max(len(x.binary_vec), len(y.binary_vec))
    m = n // 2
    
    # split the binary numbers in the middle
    high1, low1 = split_number(x.binary_vec)
    high2, low2 = split_number(y.binary_vec)
    
    # recursive multiplication calls
    z0 = subquadratic_multiply(low1, low2)
    z1 = subquadratic_multiply(BinaryNumber(low1.decimal_val + high1.decimal_val), BinaryNumber(low2.decimal_val + high2.decimal_val))
    z2 = subquadratic_multiply(high1, high2)
    
    # combine results
    return z2 * 2**(2*m) + ((z1 - z2 - z0) * 2**m) + z0


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

