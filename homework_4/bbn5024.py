############################################################
# CMPSC442: Homework 4
############################################################
student_name = "Brian Nguyen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from Queue import Queue
from copy import deepcopy


############################################################
# Section 1: Sudoku
############################################################

def sudoku_cells():
    return [(i, j) for i in range(9) for j in range(9)]


def sudoku_arcs():

    arcs = []
    for i in range(9):
        for j in range(9):
            # Row arcs
            arcs += [((i, j), (i, k)) for k in range(9) if (i, j) != (i, k)]
            # Column arcs
            arcs += [((i, j), (k, j)) for k in range(9) if (i, j) != (k, j)]

    # Block arcs
    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            for r in range(i - 3, i):
                for c in range(j - 3, j):
                    arcs += [((r, c), (k, l)) for k in range(i - 3, i) for l in
                    range(j - 3, j)
                        if ((r, c), (k, l)) not in arcs and (r, c) != (k, l)]
    return arcs


def read_board(path):

    board = {}

    with open(path, "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for i, line in enumerate(content):
            for j, char in enumerate(line):
                if char == "*":
                    board[(i, j)] = set(range(1, 10))
                else:
                    board[(i, j)] = set([int(char)])
    return board


def create_arc_table(arcs):

    arc_table = {}
    for a in arcs:
        if a[1] not in arc_table:
            arc_table[a[1]] = [a]
        else:
            arc_table[a[1]].append(a)
    return arc_table


class Sudoku(object):

    CELLS = sudoku_cells()  # All possible cells
    ARCS = sudoku_arcs()  # All possible arcs
    ARC_TABLE = create_arc_table(ARCS)  # Cells and their accompanying arcs

    def __init__(self, board):
        self.board = board

    def is_solved(self):

        # Iterate through the cells to see if the board is solved
        for c in Sudoku.CELLS:
            if len(self.board[c]) != 1:
                return False
        return True

    def get_values(self, cell):

        # Return the possible values at a particular cell
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):

        # Check if any removal can be made
        if (cell1, cell2) in Sudoku.ARCS and len(self.board[cell2]) == 1 and \
        len(self.board[cell1]) != 1:
            self.board[cell1] = self.board[cell1].difference(self.board[cell2])
            return True
        return False

    def infer_ac3(self):

        # Initialize queue with all arcs
        q = Queue()
        [q.put(a) for a in Sudoku.ARCS]

        # For each arc, remove any inconsistencies
        while not q.empty():
            cell1, cell2 = q.get()
            if self.remove_inconsistent_values(cell1, cell2):
                if self.is_solved():
                    return
                # Enqueue all possibly affected arcs
                [q.put(a) for a in Sudoku.ARC_TABLE[cell1]]

    def infer_improved(self):

        # Initialize queue with all cells
        q = Queue()
        [q.put(c) for c in Sudoku.CELLS]

        # Keep track whether changes happened or not
        flag = True
        
        # Check to see if any inference can be made per cell
        while not q.empty():

            # if a change has been made run AC-3 to see if
            # inconsistencies can be removed
            if flag:
                flag = False
                if self.is_solved():
                    return
                self.infer_ac3()
                
            # Get next cell in the queue
            cell = q.get()

            if len(self.board[cell]) == 1:
                continue

            # Check for inference in rows
            s = set()
            for j in range(9):
                if j != cell[1]:
                    s = s.union(self.board[(cell[0], j)])
            diff = self.board[cell].difference(s)
            if len(diff) == 1:
                self.board[cell] = diff
                flag = True
                [q.put(c) for c in Sudoku.CELLS]
                #[q.put(c[0]) for c in Sudoku.ARC_TABLE[cell]]
                continue

            # Check for inference in columns
            s = set()
            for i in range(9):
                if i != cell[0]:
                    s = s.union(self.board[(i, cell[1])])
            diff = self.board[cell].difference(s)
            if len(diff) == 1:
                self.board[cell] = diff
                flag = True
                [q.put(c) for c in Sudoku.CELLS]
                #[q.put(c[0]) for c in Sudoku.ARC_TABLE[cell]]
                continue

            # Check for inference in blocks
            s = set()
            r = (cell[0] // 3 + 1) * 3
            c = (cell[1] // 3 + 1) * 3
            for i in range(r - 3, r):
                for j in range(c - 3, c):
                    if (i, j) != cell:
                        s = s.union(self.board[(i, j)])
            diff = self.board[cell].difference(s)
            if len(diff) == 1:
                self.board[cell] = diff
                flag = True
                [q.put(c) for c in Sudoku.CELLS]
                #[q.put(c[0]) for c in Sudoku.ARC_TABLE[cell]]

    def infer_with_guessing(self):

        # Initial Improved AC-3 Run
        self.infer_improved()

        # Keep track of states for back-tracking
        prev_board = deepcopy(self.board)

        # For each cell, make a guess if isn't solved
        for c in Sudoku.CELLS:
            if len(self.board[c]) == 1:
                continue
            else:
                # Iterate through possible choices for the cell
                for p in list(self.board[c]):

                    # Make change in board
                    self.board[c] = set([p])

                    # Remove inconsistent values from accompanying arcs
                    for c1, c2 in Sudoku.ARC_TABLE[c]:
                        self.remove_inconsistent_values(c1, c2)

                    # See if any inference can be made after change
                    self.infer_improved()

                    # If the board is solved, finish
                    if self.is_solved() or self.infer_with_guessing():
                        return True

                    # Otherwise, revert back to previous board
                    self.board = deepcopy(prev_board)

        # Revert back to previous board
        self.board = deepcopy(prev_board)
        return False


############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
6 hours.
"""

feedback_question_2 = """
It was a fun and challenging homework. No significant stumbling blocks.
"""

feedback_question_3 = """
I liked all aspects.
"""
