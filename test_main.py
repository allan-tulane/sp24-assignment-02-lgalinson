from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(999999)) == 0
    assert subquadratic_multiply(BinaryNumber(8277366), BinaryNumber(0)) == 0
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1