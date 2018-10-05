from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals


def test_section_1():

	# Getter
	p = TilePuzzle([[1, 2], [3, 0]])
	assert_equals(p.get_board(), [[1, 2], [3, 0]])
	assert_equals(p.empty_space, [1, 1])
	p = TilePuzzle([[0, 1], [3, 2]])
	assert_equals(p.get_board(), [[0, 1], [3, 2]])
	assert_equals(p.empty_space, [0, 0])

	# Create puzzles
	p = create_tile_puzzle(3, 3)
	assert_equals(p.get_board(), [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
	assert_equals(p.empty_space, [2, 2])
	p = create_tile_puzzle(2, 4)
	assert_equals(p.get_board(), [[1, 2, 3, 4], [5, 6, 7, 0]])
	assert_equals(p.empty_space, [1, 3])

	# Perform move
	p = create_tile_puzzle(3, 3)
	assert_equals(p.perform_move("up"), True)
	assert_equals(p.get_board(), [[1, 2, 3], [4, 5, 0], [7, 8, 6]])
	p = create_tile_puzzle(3, 3)
	assert_equals(p.perform_move("down"), False)
	assert_equals(p.get_board(), [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

	# Is solved
	p = TilePuzzle([[1, 2], [3, 0]])
	assert_equals(p.is_solved(), True)
	p = TilePuzzle([[0, 1], [3, 2]])
	assert_equals(p.is_solved(), False)

	# Copy
	p = create_tile_puzzle(3, 3)
	p2 = p.copy()
	assert_equals(p.get_board(), p2.get_board())
	p = create_tile_puzzle(3, 3)
	p2 = p.copy()
	p.perform_move("left")
	assert_not_equals(p.get_board(), p2.get_board())

	# Successors
	print("\n ### Successors ### \n")
	p = create_tile_puzzle(3, 3)
	for move, new_p in p.successors():
		print move, new_p.get_board()

	print("\n ################## \n")

	b = [[1,2,3], [4,0,5], [6,7,8]]
	p = TilePuzzle(b)
	for move, new_p in p.successors():
		print move, new_p.get_board()

	print("\n ################## \n")

	# Iterative Deepening Search
	p = create_tile_puzzle(3, 3)
	solutions = p.find_solutions_iddfs()
	assert_equals(list(solutions), [[]])

	b = [[4,1,2], [0,5,3], [7,8,6]]
	p = TilePuzzle(b)
	solutions = p.find_solutions_iddfs()
	assert_equals(next(solutions), ['up', 'right', 'right', 'down', 'down'])

	b = [[1,2,3], [4,0,8], [7,6,5]]
	p = TilePuzzle(b)
	solutions = p.find_solutions_iddfs()
	assert_equals(list(p.find_solutions_iddfs()), [['down', 'right', 'up',
		'left', 'down', 'right'], ['right', 'down', 'left', 'up', 'right', 'down']])

	# A Star Search
	b = [[4,1,2], [0,5,3], [7,8,6]]
	p = TilePuzzle(b)
	assert_equals(p.find_solution_a_star(), ['up', 'right', 'right', 'down', 'down'])
	b = [[1,2,3], [4,0,5], [6,7,8]]
	p = TilePuzzle(b)
	assert_equals(p.find_solution_a_star(), ['right', 'down', 'left', 'left',
		'up','right', 'down', 'right', 'up', 'left','left', 'down', 'right',
		'right'])


def test_section_2():
	
	scene = [[False, False, False], [False, True , False], [False, False, False]]
	assert_equals(find_path((0, 0), (2, 1), scene), [(0, 0), (1, 0), (2, 1)])
	scene = [[False, True, False], [False, True, False], [False, True, False]]
	assert_equals(find_path((0, 0), (0, 2), scene), None)

def test_section_3():

	assert_equals(solve_distinct_disks(4, 2), [(0, 2), (2, 3), (1, 2)])
	assert_equals(solve_distinct_disks(5, 2), [(0, 2), (1, 3), (2, 4)])
	assert_equals(solve_distinct_disks(4, 3), [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3), (0, 1)])
	assert_equals(solve_distinct_disks(5, 3), [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)])


def test_section_4():

	# Getter
	b = [[False, False], [False, False]]
	g = DominoesGame(b)
	assert_equals(g.get_board(), [[False, False], [False, False]])
	b = [[True, False], [True, False]]
	g = DominoesGame(b)
	assert_equals(g.get_board(), [[True, False], [True, False]])

	# Create game
	g = create_dominoes_game(2, 2)
	assert_equals(g.get_board(), [[False, False], [False, False]])
	g = create_dominoes_game(2, 3)
	assert_equals(g.get_board(), [[False, False, False], [False, False, False]])

	# Reset
	b = [[False, False], [False, False]]
	g = DominoesGame(b)
	g.reset()
	assert_equals(g.get_board(), [[False, False], [False, False]])
	b = [[True, False], [True, False]]
	g = DominoesGame(b)
	g.reset()
	assert_equals(g.get_board(), [[False, False], [False, False]])

	# Legal move
	b = [[False, False], [False, False]]
	g = DominoesGame(b)
	assert_equals(g.is_legal_move(0, 0, True), True)
	assert_equals(g.is_legal_move(0, 0, False), True)
	b = [[True, False], [True, False]]
	g = DominoesGame(b)
	assert_equals(g.is_legal_move(0, 0, False), False)
	assert_equals(g.is_legal_move(0, 1, True), True)
	assert_equals(g.is_legal_move(1, 1, True), False)

	# Legal moves
	g = create_dominoes_game(3, 3)
	assert_equals(list(g.legal_moves(True)), [(0, 0), (0, 1), (0, 2), (1, 0),
		(1, 1), (1, 2)])
	assert_equals(list(g.legal_moves(False)), [(0, 0), (0, 1), (1, 0), (1, 1),
		(2, 0), (2, 1)])
	b = [[True, False], [True, False]]
	g = DominoesGame(b)
	assert_equals(list(g.legal_moves(True)), [(0, 1)])
	assert_equals(list(g.legal_moves(False)), [])

	# Perform move
	g = create_dominoes_game(3, 3)
	g.perform_move(0, 1, True)
	assert_equals(g.get_board(), [[False, True, False], [False, True, False],
		[False, False, False]])
	g = create_dominoes_game(3, 3)
	g.perform_move(1, 0, False)
	assert_equals(g.get_board(), [[False, False, False], [True, True, False],
		[False, False, False]])

	# Game over
	b = [[False, False], [False, False]]
	g = DominoesGame(b)
	assert_equals(g.game_over(True), False)
	assert_equals(g.game_over(False), False)
	b = [[True, False], [True, False]]
	g = DominoesGame(b)
	assert_equals(g.game_over(True), False)
	assert_equals(g.game_over(False), True)

	# Copy
	g = create_dominoes_game(4, 4)
	g2 = g.copy()
	assert_equals(g.get_board(), g2.get_board())
	g = create_dominoes_game(4, 4)
	g2 = g.copy()
	g.perform_move(0, 0, True)
	assert_not_equals(g.get_board(), g2.get_board())

	# Successors
	b = [[False, False], [False, False]]
	g = DominoesGame(b)
	for m, new_g in g.successors(True):
		print m, new_g.get_board()
	print("#############################")
	b = [[True, False], [True, False]]
	g = DominoesGame(b)
	for m, new_g in g.successors(True):
		print m, new_g.get_board()


if __name__ == "__main__":
	print "\n########## Testing Section 1 ##########\n"
	test_section_1()
	print "\n########## Testing Section 2 ##########\n"
	test_section_2()
	print "\n########## Testing Section 3 ##########\n"
	test_section_3()
	print "\n########## Testing Section 4 ##########\n"
	test_section_4()
