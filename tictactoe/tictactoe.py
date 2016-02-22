import unittest


class TicTacToe:
    def __init__(self):
        self.grid = {i: {j: '' for j in range(3)} for i in range(3)}


class TicTacToeTests(unittest.TestCase):
    def test_grid(self):
        ttt = TicTacToe()
        expected = {
            0: {
                0: '',
                1: '',
                2: ''
            },
            1: {
                0: '',
                1: '',
                2: ''
            },
            2: {
                0: '',
                1: '',
                2: ''
            }
        }
        self.assertEqual(expected, ttt.grid)

if __name__ == '__main__':
    # tests will be executed here
    unittest.main()

