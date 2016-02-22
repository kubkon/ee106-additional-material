import unittest


class TicTacToe:
    def __init__(self):
        self.grid = {i: {j: '' for j in range(3)} for i in range(3)}

    def check_if_done(self):
        done = True
        for i in range(3):
            row = ''
            for j in range(3):
                if self.grid[i][j] == '':
                    done = False

                row += self.grid[i][j]

            if row == 'xxx' or row == 'ooo':
                done = True
                break

        for j in range(3):
            column = ''
            for i in range(3):
                column += self.grid[i][j]

            if column == 'xxx' or column == 'ooo':
                done = True
                break
                
        return done


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

    def test_check_if_done_rows(self):
        ttt = TicTacToe()
        ttt.grid[0][0] = 'x'
        ttt.grid[0][1] = 'x'
        ttt.grid[0][2] = 'x'
        self.assertEqual(True, ttt.check_if_done())

        ttt = TicTacToe()
        ttt.grid[1][0] = 'o'
        ttt.grid[1][1] = 'o'
        ttt.grid[1][2] = 'o'
        self.assertEqual(True, ttt.check_if_done())

        ttt = TicTacToe()
        ttt.grid[2][0] = 'o'
        ttt.grid[2][1] = 'o'
        ttt.grid[2][2] = 'o'
        self.assertEqual(True, ttt.check_if_done())

    def test_check_if_done_columns(self):
        ttt = TicTacToe()
        ttt.grid[0][0] = 'x'
        ttt.grid[1][0] = 'x'
        ttt.grid[2][0] = 'x'
        self.assertEqual(True, ttt.check_if_done())

        ttt = TicTacToe()
        ttt.grid[0][1] = 'x'
        ttt.grid[1][1] = 'x'
        ttt.grid[2][1] = 'x'
        self.assertEqual(True, ttt.check_if_done())
        
        ttt = TicTacToe()
        ttt.grid[0][2] = 'x'
        ttt.grid[1][2] = 'x'
        ttt.grid[2][2] = 'x'
        self.assertEqual(True, ttt.check_if_done())

    def test_check_if_done_no_more_moves(self):
        ttt = TicTacToe()
        ttt.grid[0][0] = 'x'
        ttt.grid[0][1] = 'x'
        ttt.grid[1][0] = 'x'
        self.assertEqual(False, ttt.check_if_done())

        ttt = TicTacToe()
        ttt.grid[0][0] = 'x'
        ttt.grid[0][1] = 'o'
        ttt.grid[0][2] = 'x'
        ttt.grid[1][0] = 'o'
        ttt.grid[1][1] = 'x'
        ttt.grid[1][2] = 'o'
        ttt.grid[2][0] = 'x'
        ttt.grid[2][1] = 'o'
        ttt.grid[2][2] = 'x'
        self.assertEqual(True, ttt.check_if_done())

if __name__ == '__main__':
    # tests will be executed here
    unittest.main()

