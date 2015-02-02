import unittest

def square(x):
    return x**2

class Tests(unittest.TestCase):
    def test_square(self):
        given = square(4)
        expected = 16
        self.assertEqual(given, expected)

if __name__ == '__main__':
    unittest.main()
