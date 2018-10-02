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


if __name__ == "__main__":
	test_section_1()