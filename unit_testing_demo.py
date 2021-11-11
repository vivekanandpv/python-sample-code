import unittest


def square(n):
    return n*n


class SquareTests(unittest.TestCase):
    def test_square_returns_square_of_a_number(self):
        self.assertEquals(square(3), 10, 'Well this test fails!')


if __name__ == '__main__':
    unittest.main(verbosity=2)
