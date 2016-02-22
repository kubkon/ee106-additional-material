import unittest


class TicTacToe:
    def __init__(self):
        self.grid = {i: {j: '' for j in range(3)} for i in range(3)}

    def check_if_done(self):
        # check if rows contain winning possibility
        for i in range(3):
            row = ''
            for j in range(3):
                row += self.grid[i][j]

            if row == 'xxx' or row == 'ooo':
                return True

        # check if columns contain winning possibility
        for j in range(3):
            column = ''
            for i in range(3):
                column += self.grid[i][j]

            if column == 'xxx' or column == 'ooo':
                return True

        # check if diagonals contain winning possibility
        for l in [[(0,0), (1,1), (2,2)], [(2,0), (1,1), (0,2)]]:
            diagonal = ''
            for (i,j) in l:
                diagonal += self.grid[i][j]

            if diagonal == 'xxx' or diagonal == 'ooo':
                return True

        # finally, check if there are moves remaining
        done = True
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == '':
                    done = False
                
        return done

    def render(self):
        rendered = ''
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == '':
                    rendered += '_ '
                else:
                    rendered += self.grid[i][j] + ' '
            rendered += '\n'
        return rendered


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

    def test_check_if_done_diagonal(self):
        ttt = TicTacToe()
        ttt.grid[0][0] = 'x'
        ttt.grid[1][1] = 'x'
        ttt.grid[2][2] = 'x'
        self.assertEqual(True, ttt.check_if_done())

        ttt = TicTacToe()
        ttt.grid[2][0] = 'x'
        ttt.grid[1][1] = 'x'
        ttt.grid[0][2] = 'x'
        self.assertEqual(True, ttt.check_if_done())

    def test_render(self):
        ttt = TicTacToe()
        self.assertEqual('_ _ _ \n_ _ _ \n_ _ _ \n', ttt.render())

        ttt.grid[0][0] = 'x'
        self.assertEqual('x _ _ \n_ _ _ \n_ _ _ \n', ttt.render())

        ttt.grid[2][2] = 'o'
        self.assertEqual('x _ _ \n_ _ _ \n_ _ o \n', ttt.render())

        ttt.grid[0][2] = 'x'
        self.assertEqual('x _ x \n_ _ _ \n_ _ o \n', ttt.render())

        ttt.grid[0][1] = 'o'
        self.assertEqual('x o x \n_ _ _ \n_ _ o \n', ttt.render())


if __name__ == '__main__':
    # tests will be executed here
    unittest.main()

