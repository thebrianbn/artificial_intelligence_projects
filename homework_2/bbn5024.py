############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Brian Nguyen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from copy import deepcopy
from itertools import permutations
from math import factorial
import random
from Queue import Queue


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    board_size = n * n
    return factorial(board_size) / (factorial(n) * factorial(board_size -
        n))

def num_placements_one_per_row(n):
    return n ** n

def n_queens_valid(board):
    pairs = [(row, col) for row, col in enumerate(board)]
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if pairs[i] == pairs[j]:
                continue
            # Test if pairs are in same column
            elif pairs[i][1] == pairs[j][1]:
                return False
            # Test if pairs are diagonal
            else:
                row_diff = abs(pairs[i][0] - pairs[j][0])
                col_diff = abs(pairs[i][1] - pairs[j][1])
                if row_diff == col_diff:
                    return False
    return True


def n_queens_solutions(n):
    possible = map(list, list(permutations(range(n))))
    for board in possible:
        if n_queens_valid(board):
            yield board

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.lrow = len(board)
        self.lcol = len(board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):

        # Center
        if self.board[row][col]:
            self.board[row][col] = False
        else:
            self.board[row][col] = True

        # Right
        if col < self.lcol - 1:
            if self.board[row][col + 1]:
                self.board[row][col + 1] = False
            else:
                self.board[row][col + 1] = True

        # Left
        if col > 0:
            if self.board[row][col - 1]:
                self.board[row][col - 1] = False
            else:
                self.board[row][col - 1] = True

        # Up
        if row > 0:
            if self.board[row - 1][col]:
                self.board[row - 1][col] = False
            else:
                self.board[row - 1][col] = True

        # Down
        if row < self.lrow - 1:
            if self.board[row + 1][col]:
                self.board[row + 1][col] = False
            else:
                self.board[row + 1][col] = True

    def scramble(self):
        for i in range(self.lrow):
            for j in range(self.lcol):
                if random.random() >= 0.5:
                    self.perform_move(i, j)

    def is_solved(self):

        if not sum(map(sum, self.board)):
            return True
        return False

    def copy(self):

        return LightsOutPuzzle(deepcopy(self.board))

    def successors(self):
        for i in range(self.lrow):
            for j in range(self.lcol):
                board_copy = self.copy()
                board_copy.perform_move(i, j)
                yield (i, j), board_copy

    def find_solution(self):

        # Initial data structures
        q = Queue()
        visited = set()

        # Add initial state to queue
        q.put(([], self))

        while not q.empty():
            # Retrieve next state from queue and remove
            moves, current = q.get()

            # Check if the state is solved
            if current.is_solved():
                return moves

            # Convert state to be friendly with sets
            state = tuple(map(tuple, current.get_board()))

            # Check if state has already been visited
            if state in visited:
                continue
            else:
                visited.add(state)

            # Add successors of the state to queue
            for move, new_p in current.successors():
                new_moves = deepcopy(moves)
                new_moves.append(move)
                q.put((new_moves, new_p))

        # If queue is empty and no solutions are found, return None
        return None

def create_puzzle(rows, cols):
    return LightsOutPuzzle([[False for j in range(cols)] for i in range(rows)])

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):

    # Initial data structures
    q = Queue()
    visited = []
    state = []

    # Create initial state as an array of 1s and 0s, put into queue
    state = [1 if i < n else 0 for i in range(length)]
    q.put(([], state))

    # While the queue isn't empty, enqueue adjacent disks of current
    # For this one, it's never a need for a disk to go backwards
    while not q.empty():
        # Retrieve next state from queue
        moves, current = q.get()
        # Check if goal state is reached
        if sum(current[length - n:]) == n:
            return moves
        # Check if state is already visited
        if current in visited:
            continue
        else:
            visited.append(current)
        # Enqueue all possible moves
        for i in range(length - 1):
            if current[i + 1] == 0 and current[i] == 1:
                one_hop = deepcopy(current)
                one_hop[i] = 0
                one_hop[i + 1] = 1
                new_moves1 = deepcopy(moves)
                new_moves1.append((i, i + 1))
                q.put((new_moves1, one_hop))
            if length - i != 2:  # Prevent index error
                if current[i + 2] == 0 and current[i + 1] == 1 and \
                current[i] == 1:
                    two_hop = deepcopy(current)
                    two_hop[i] = 0
                    two_hop[i + 2] = 1
                    new_moves2 = deepcopy(moves)
                    new_moves2.append((i, i + 2))
                    q.put((new_moves2, two_hop))
    # If no possible moves left, return None
    return None


def solve_distinct_disks(length, n):
    
    # Initial data structures
    q = Queue()
    visited = []

    # Create initial state as an array of 1s and 0s, put into queue
    state = [i if i < n + 1 else 0 for i in range(1, length + 1)]
    q.put(([], state))

    # While the queue isn't empty, enqueue adjacent disks of current
    while not q.empty():
        # Retrieve next state from queue
        moves, current = q.get()
        # Check if goal state is reached
        if sorted(current[length - n:], reverse=True) == current[length - n:] and \
        0 not in current[length - n:]:
            return moves
        # Check if state is already visited
        if current in visited:
            continue
        else:
            visited.append(current)
        # Enqueue all possible moves
        for i in range(length):
            if i < length - 1:
                if current[i + 1] == 0 and current[i] != 0:
                    one_hop = deepcopy(current)
                    temp = one_hop[i]
                    one_hop[i] = 0
                    one_hop[i + 1] = temp
                    new_moves1 = deepcopy(moves)
                    new_moves1.append((i, i + 1))
                    q.put((new_moves1, one_hop))
            if i < length - 2:  # Prevent index error
                if current[i + 2] == 0 and current[i + 1] != 0 and \
                current[i] != 0:
                    two_hop = deepcopy(current)
                    temp = two_hop[i]
                    two_hop[i] = 0
                    two_hop[i + 2] = temp
                    new_moves2 = deepcopy(moves)
                    new_moves2.append((i, i + 2))
                    q.put((new_moves2, two_hop))
            if i > 0:
                if current[i - 1] == 0 and current[i] != 0:
                    one_back = deepcopy(current)
                    temp = one_back[i]
                    one_back[i] = 0
                    one_back[i - 1] = temp
                    new_moves3 = deepcopy(moves)
                    new_moves3.append((i, i - 1))
                    q.put((new_moves3, one_back))
            if i > 1:
                if current[i - 2] == 0 and current[i - 1] != 0 and \
                current[i] != 0:
                    two_back = deepcopy(current)
                    temp = two_back[i]
                    two_back[i] = 0
                    two_back[i - 2] = temp
                    new_moves4 = deepcopy(moves)
                    new_moves4.append((i, i - 2))
                    q.put((new_moves4, two_back))
    # If no possible moves left, return None
    return None

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
4.5 hours.
"""

feedback_question_2 = """
Making sure breadth-first-search was working correctly for all of the cases
was the most difficult challenge. No significant stumbling blocks.
"""

feedback_question_3 = """
It was a fun homework! Nothing I would change.
"""
