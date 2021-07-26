# Test-Driven Development(TDD): A process in which the programmer writes the tests before writing the code.

# RED STAGE: start here, write a test, test fails

# GREEN STAGE: Write code to make test pass, code then passes test

# REFACTOR STAGE: Workable code, how to improve? Clean code at the end


import unittest

def product(a, b):
    total = 0
    for i in range(a):
        total += b
    return total 
    # return a * b   this tis the refactor stage, this is much simpler than all the lines above


class TestProduct(unittest.TestCase):
    def test_multiplies_two_numbers_together(self):
        self.assertEqual(
            product(3, 5),
            15
        )

if __name__ == "__main__":
    unittest.main()