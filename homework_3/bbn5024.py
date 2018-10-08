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
import math
from Queue import PriorityQueue


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

    opposite = {"up": "down",
                "down": "up",
                "left": "right",
                "right": "left"}
    
    # Required
    def __init__(self, board):
        self.board = board
        self.rlen = len(board)
        self.clen = len(board[0])
        self.tile_dict = {}
        

        counter = 1
        end = self.rlen * self.clen
        for i in range(self.rlen):
            for j in range(self.clen):
                if counter == end:
                    self.tile_dict[0] = (i, j)
                else:
                    self.tile_dict[counter] = (i, j)
                counter += 1

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
        counter = 1
        end = self.rlen * self.clen
        for i in range(self.rlen):
            for j in range(self.clen):
                if counter == end and self.board[i][j] == 0:
                    continue
                elif self.board[i][j] != counter:
                    return False
                counter += 1
        return True

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
        recent_move = moves[-1]
        if recent_move[1].is_solved():
            yield map(lambda x: x[0], moves)

        if limit == 0:
            return
        else:
            next_successors = list(recent_move[1].successors())
            for move in next_successors:
                if TilePuzzle.opposite[move[0]] == recent_move[0]:
                    continue
                moves_copy = copy.copy(moves)
                moves_copy.append(move)
                for x in self.iddfs_helper(limit - 1, moves_copy):
                    yield x

    # Required
    def find_solutions_iddfs(self):
        flag = False
        counter = 0
        while True:
            temp = self.iddfs_helper(counter, [(None, self)])
            for x in temp:
                flag = True
                yield x[1:]
            if flag:
                break
            counter += 1

    def get_md(self, board):

        # Calculate Manhattan Distance
        md_sum = 0
        for i in range(self.rlen):
            for j in range(self.clen):
                tile = board.board[i][j]
                solved_location = self.tile_dict[tile]
                md_sum += abs(i - solved_location[0]) + abs(j - solved_location[1])
        return md_sum

    # Required
    def find_solution_a_star(self):
        pq = PriorityQueue()

        # Enqueue initial successors
        successors = self.successors()
        for move, new_p in successors:
            md = self.get_md(new_p)
            pq.put((md, ([move], new_p)))

        # Enqueue successors until solution is found
        while not pq.empty():
            # Get puzzle with lowest heuristic, set variables
            puzzle = pq.get()
            md = puzzle[0]
            moves = puzzle[1][0]
            new_p = puzzle[1][1]

            # Check if solved
            if new_p.is_solved():
                return moves
            
            # Add successors to priority queue
            successors = new_p.successors()
            for move, new_p in successors:
                if TilePuzzle.opposite[move] == moves[-1]:
                    continue
                moves_copy = copy.copy(moves)
                moves_copy.append(move)
                new_md = self.get_md(new_p)
                pq.put((md + new_md, (moves_copy, new_p)))


############################################################
# Section 2: Grid Navigation
############################################################

def find_path(start, goal, scene):

    rlen = len(scene)
    clen = len(scene[0])

    def successors(point):
        x, y = point
        succ = []

        #Up
        if x - 1 >= 0 and not scene[x-1][y]:
            succ.append((x-1, y))

        # Down
        if x + 1 < rlen and not scene[x+1][y]:
            succ.append((x+1, y))

        # Left
        if y - 1 >= 0 and not scene[x][y-1]:
            succ.append((x, y-1))

        # Right
        if y + 1 < clen and not scene[x][y+1]:
            succ.append((x, y+1))

        # Up-left
        if x - 1 >= 0 and y - 1 >= 0 and not scene[x-1][y-1]:
            succ.append((x-1, y-1))

        # Up-right
        if x - 1 >= 0 and y + 1 < clen and not scene[x-1][y+1]:
            succ.append((x-1, y+1))

        # Down-left
        if x + 1 < rlen and y - 1 >= 0 and not scene[x+1][y-1]:
            succ.append((x+1, y-1))

        # Down-right
        if x + 1 < rlen and y + 1 < clen and not scene[x+1][y+1]:
            succ.append((x+1, y+1))

        return succ

    def euclid(start, end):
        return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

    # Handle obstacle at start or goal
    if scene[start[0]][start[1]] or scene[goal[0]][goal[1]]:
        return None

    # Get lengths
    rlen = len(scene)
    clen = len(scene[0])
    pq = PriorityQueue()

    # Enqueue initial successors
    succ = successors(start)
    for s in succ:
        euc = euclid(s, goal)
        pq.put((euc, [start, s]))

    # Enqueue successors until solution is found
    while not pq.empty():
        euc, path = pq.get()
        if path[-1] == goal:
            return path
        
        succ = successors(path[-1])
        for s in succ:
            if s == path[-2]:
                continue
            new_euc = euclid(s, goal)
            path_copy = copy.copy(path)
            path_copy.append(s)
            pq.put((euc + new_euc, path_copy))
    return None

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

def solve_distinct_disks(length, n):

    solution = [j if i > length - n else 0 for i, j in enumerate(range(length, 0, -1), 1)]
    state = [i if i < n + 1 else 0 for i in range(1, length + 1)]

    def successors(current):
        pass

    def heuristic(board):
        total = 0
        for i in range(length):
            if board[i] != 0:
                total += abs(i - solution.index(board[i]))
        return total

    pq = PriorityQueue()
    pq.put((0, ([], state)))

    while not pq.empty():
        cost, state = pq.get()
        moves, current = state
        if current == solution:
            return moves
        for i in range(length):
            if i < length - 1:
                if current[i + 1] == 0 and current[i] != 0:
                    one_hop = copy.copy(current)
                    temp = one_hop[i]
                    one_hop[i] = 0
                    one_hop[i + 1] = temp
                    new_moves1 = copy.deepcopy(moves)
                    new_moves1.append((i, i + 1))
                    new_cost = heuristic(one_hop)
                    pq.put((cost + new_cost, (new_moves1, one_hop)))
            if i < length - 2:  # Prevent index error
                if current[i + 2] == 0 and current[i + 1] != 0 and \
                current[i] != 0:
                    two_hop = copy.copy(current)
                    temp = two_hop[i]
                    two_hop[i] = 0
                    two_hop[i + 2] = temp
                    new_moves2 = copy.deepcopy(moves)
                    new_moves2.append((i, i + 2))
                    new_cost = heuristic(two_hop)
                    pq.put((cost + new_cost, (new_moves2, two_hop)))
            if i > 0:
                if current[i - 1] == 0 and current[i] != 0:
                    one_back = copy.copy(current)
                    temp = one_back[i]
                    one_back[i] = 0
                    one_back[i - 1] = temp
                    new_moves3 = copy.deepcopy(moves)
                    new_moves3.append((i, i - 1))
                    new_cost = heuristic(two_hop)
                    pq.put((cost + new_cost, (new_moves3, one_back)))
            if i > 1:
                if current[i - 2] == 0 and current[i - 1] != 0 and \
                current[i] != 0:
                    two_back = copy.copy(current)
                    temp = two_back[i]
                    two_back[i] = 0
                    two_back[i - 2] = temp
                    new_moves4 = copy.deepcopy(moves)
                    new_moves4.append((i, i - 2))
                    new_cost = heuristic(two_hop)
                    pq.put((cost + new_cost,(new_moves4, two_back)))
    return None

    
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
        for move in self.legal_moves(vertical):
            new_board = self.copy()
            new_board.perform_move(move[0], move[1], vertical)
            yield move, new_board

    def get_random_move(self, vertical):
        moves = list(self.legal_moves(vertical))
        return random.choice(moves)

    # Required
    def get_best_move(self, vertical, limit):

        counter = 0
        
        def eval(state):
            player_moves = len(list(state.legal_moves(vertical)))
            oppenent_moves = len(list(state.legal_moves(not vertical)))
            return player_moves - oppenent_moves

        def ab_search(state):
            v = max_value(state, float("inf"), float("-inf"), limit)
            for move, new_board in state.successors(vertical):
                if eval(new_board) == v:
                    return move, v, counter

        def max_value(state, a, b, limit):

            if limit <= 0 or state.game_over(vertical):
                print "Limit:", limit
                return eval(state)
            v = float("-inf")
            for new_state in state.successors(vertical):
                v = max([v, min_value(new_state[1], a, b, limit - 1)])
                if v >= b:
                    return v
                a = max([a, v])
            return v

        def min_value(state, a, b, limit):

            if limit <= 0 or state.game_over(vertical):
                print "Limit:", limit
                return eval(state)
            v = float("inf")
            for new_state in state.successors(vertical):
                v = min([v, max_value(new_state[1], a, b, limit - 1)])
                if v <= a:
                    return v
                b = min([b, v])
            return v

        return ab_search(self)

############################################################
# Section 5: Feedback
############################################################

feedback_question_1 = """
6 hours.
"""

feedback_question_2 = """
I found programming IDDFS and A* Star Search challenging at first.
No significant stumbling blocks.
"""

feedback_question_3 = """
I liked all of the sections.
"""
