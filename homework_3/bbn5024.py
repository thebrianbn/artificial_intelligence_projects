############################################################
# CMPSC 442: Homework 3
############################################################

student_name = "Brian Nguyen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.



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
        for i in range(self.rlen):
            for j in range(self.clen):
                if board[i][j] == 0:
                    self.empty_space = [i, j]

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        if direction == "up":
            pass
        elif direction == "down":
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            pass

    def scramble(self, num_moves):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
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
    pass

class DominoesGame(object):

    # Required
    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def reset(self):
        pass

    def is_legal_move(self, row, col, vertical):
        pass

    def legal_moves(self, vertical):
        pass

    def perform_move(self, row, col, vertical):
        pass

    def game_over(self, vertical):
        pass

    def copy(self):
        pass

    def successors(self, vertical):
        pass

    def get_random_move(self, vertical):
        pass

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
