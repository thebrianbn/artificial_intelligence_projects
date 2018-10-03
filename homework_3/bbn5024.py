############################################################
# CMPSC 442: Homework 3
############################################################

student_name = "Brian Nguyen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
import copy


############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    puzzle = []
    counter = 1
    end = rows * cols
    for i in range(rows):
        temp = []
        for j in range(cols):
            if counter == end:
                temp.append(0)
            else:
                temp.append(counter)
            counter += 1
        puzzle.append(temp)
    return TilePuzzle(puzzle)

class TilePuzzle(object):
    
    # Required
    def __init__(self, board):
        self.board = board
        self.rlen = len(board)
        self.clen = len(board[0])

        # Find empty space
        for i in range(self.rlen):
            for j in range(self.clen):
                if board[i][j] == 0:
                    self.empty_space = [i, j]

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        orig_r = self.empty_space[0]
        orig_c = self.empty_space[1]
        row = self.empty_space[0]
        col = self.empty_space[1]

        if direction == "up":
            row -= 1
        elif direction == "down":
            row += 1
        elif direction == "left":
            col -= 1
        elif direction == "right":
            col += 1

        if row < 0 or row >= self.rlen or col < 0 or col >= self.clen:
            return False
        else:
            self.board[orig_r][orig_c], self.board[row][col] = \
                self.board[row][col], self.board[orig_r][orig_c]
            self.empty_space = [row, col]
        return True

    def scramble(self, num_moves):
        possible_moves = ["up", "down", "left", "right"]
        for i in range(num_moves):
            self.perform_move(random.choice(possible_moves))

    def is_solved(self):
        if self.empty_space == [self.rlen - 1, self.clen - 1]:
            return True
        return False

    def copy(self):
        puzzle = copy.deepcopy(self.board)
        return TilePuzzle(puzzle)

    def successors(self):
        possible_moves = ["up", "down", "left", "right"]
        for move in possible_moves:
            new_p = self.copy()
            if new_p.perform_move(move):
                yield move, new_p

    def iddfs_helper(self, limit, moves):
        pass

    # Required
    def find_solutions_iddfs(self):
        pass

    # Required
    def find_solution_a_star(self):
        pass

############################################################
# Section 2: Grid Navigation
############################################################

def find_path(start, goal, scene):
    pass

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    board = [[False for j in range(cols)] for i in range(rows)]
    return DominoesGame(board)

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rlen = len(board)
        self.clen = len(board[0])

    def get_board(self):
        return self.board

    def reset(self):
        for i in range(self.rlen):
            for j in range(self.clen):
                self.board[i][j] = False

    def is_legal_move(self, row, col, vertical):

        # Initial placement check
        if self.board[row][col]:
            return False

        if vertical:
            row += 1
        else:
            col += 1

        # Adjacent placement check
        if row >= self.rlen or col >= self.clen or self.board[row][col]:
            return False

        return True


    def legal_moves(self, vertical):

        for i in range(self.rlen):
            for j in range(self.clen):
                if self.is_legal_move(i, j, vertical):
                    yield i, j

    def perform_move(self, row, col, vertical):

        self.board[row][col] = True
        if vertical:
            self.board[row + 1][col] = True
        else:
            self.board[row][col+1] = True

    def game_over(self, vertical):
        if list(self.legal_moves(vertical)) == []:
            return True
        return False

    def copy(self):
        board = copy.deepcopy(self.board)
        return DominoesGame(board)

    def successors(self, vertical):
        moves = list(self.legal_moves(vertical))
        for move in moves:
            new_board = self.copy()
            new_board.perform_move(move[0], move[1], vertical)
            yield move, new_board

    def get_random_move(self, vertical):
        moves = list(self.legal_moves(vertical))
        return random.choice(moves)

    # Required
    def get_best_move(self, vertical, limit):
        pass

############################################################
# Section 5: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
