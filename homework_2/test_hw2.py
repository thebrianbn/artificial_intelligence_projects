from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals

def test_section_1():

	assert_equals(num_placements_all(2), 6)
	assert_equals(num_placements_all(3), 84)

	assert_equals(num_placements_one_per_row(2), 4)
	assert_equals(num_placements_one_per_row(3), 27)

	assert_equals(n_queens_valid([0, 0]), False)
	assert_equals(n_queens_valid([0, 2]), True)
	assert_equals(n_queens_valid([0, 1]), False)
	assert_equals(n_queens_valid([0, 3, 1]), True)

	solutions = n_queens_solutions(4)
	assert_equals(next(solutions), [1, 3, 0, 2])
	assert_equals(next(solutions), [2, 0, 3, 1])
	assert_equals(len(list(n_queens_solutions(8))), 92)
	print(list(n_queens_solutions(6)))
	assert_equals(len(list(n_queens_solutions(6))), 4)
	assert_equals(list(n_queens_solutions(6)), [[1, 3, 5, 0, 2, 4], [2, 5, 1, 4, 0, 3],
 				  [3, 0, 4, 1, 5, 2], [4, 2, 0, 5, 3, 1]])


def test_section_2():

	b = [[True, False], [False, True]]
	p = LightsOutPuzzle(b)
	assert_equals(p.get_board(), [[True, False], [False, True]])
	b = [[True, True], [True, True]]
	p = LightsOutPuzzle(b)
	assert_equals(p.get_board(), [[True, True], [True, True]])


	p = create_puzzle(2, 2)
	assert_equals(p.get_board(), [[False, False], [False, False]])
	p = create_puzzle(2, 3)
	assert_equals(p.get_board(), [[False, False, False], [False, False, False]])

	p = create_puzzle(3, 3)
	p.perform_move(1, 1)
	assert_equals(p.get_board(), [[False, True, False], [True, True, True ], [False, True, False]])
	p = create_puzzle(3, 3)
	p.perform_move(0, 0)
	assert_equals(p.get_board(), [[True, True, False], [True, False, False], [False, False, False]])

	b = [[True, False], [False, True]]
	p = LightsOutPuzzle(b)
	assert_equals(p.is_solved(), False)
	b = [[False, False], [False, False]]
	p = LightsOutPuzzle(b)
	assert_equals(p.is_solved(), True)

	p = create_puzzle(3, 3)
	p2 = p.copy()
	assert_equals(p.get_board(), p2.get_board())
	p = create_puzzle(3, 3)
	p2 = p.copy()
	p.perform_move(1, 1)
	assert_not_equals(p.get_board(), p2.get_board())

	p = create_puzzle(2, 2)
	for move, new_p in p.successors():
		print move, new_p.get_board()
	for i in range(2, 6):
		p = create_puzzle(i, i + 1)
		print len(list(p.successors()))

	p = create_puzzle(2, 3)
	for row in range(2):
		for col in range(3):
			p.perform_move(row, col)
	print(p.find_solution())
	b = [[False, False, False], [False, False, False]]
	b[0][0] = True
	p = LightsOutPuzzle(b)
	print p.find_solution() is None

	p = create_puzzle(3, 3)
	for row in range(3):
		for col in range(3):
			p.perform_move(row, col)
	print(p.find_solution())


def test_section_3():

	assert_equals(solve_identical_disks(4, 2), [(0, 2), (1, 3)])
	assert_equals(solve_identical_disks(5, 2), [(0, 2), (1, 3), (2, 4)])
	assert_equals(solve_identical_disks(4, 3), [(1, 3), (0, 1)])
	assert_equals(solve_identical_disks(5, 3), [(1, 3), (0, 1), (2, 4), (1, 2)])

	assert_equals(solve_distinct_disks(4, 2), [(0, 2), (2, 3), (1, 2)])
	assert_equals(solve_distinct_disks(5, 2), [(0, 2), (1, 3), (2, 4)])
	assert_equals(solve_distinct_disks(4, 3), [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3), (0, 1)])
	assert_equals(solve_distinct_disks(5, 3), [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)])

if __name__ == "__main__":
	print "Testing Section 1"
	test_section_1()
	print "Testing Section 2"
	test_section_2()
	print "Testing Section 3"
	test_section_3()