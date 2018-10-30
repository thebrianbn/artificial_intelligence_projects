from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals


def test_section_1():
	b = read_board("hw4-medium1.txt")
	assert_equals(Sudoku(b).get_values((0, 0)), set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
	assert_equals(Sudoku(b).get_values((0, 1)), set([1]))

	
	arcs = sudoku_arcs()
	assert_equals(((0, 0), (0, 8)) in sudoku_arcs(), True)
	assert_equals(((0, 0), (8, 0)) in sudoku_arcs(), True)
	assert_equals(((0, 8), (0, 0)) in sudoku_arcs(), True)
	assert_equals(((0, 0), (2, 1)) in sudoku_arcs(), True)
	assert_equals(((2, 2), (0, 0)) in sudoku_arcs(), True)
	assert_equals(((2, 3), (0, 0)) in sudoku_arcs(), False)
	
	sudoku = Sudoku(read_board("hw4-easy.txt"))
	for col in [0, 1, 4]:
		removed = sudoku.remove_inconsistent_values((0, 3), (0, col))
		print removed, sudoku.get_values((0, 3))

def test_section_2():
	sudoku = Sudoku(read_board("hw4-easy.txt"))
	sudoku.infer_ac3()
	sudoku.print_board()

def test_section_3():
	sudoku = Sudoku(read_board("hw4-medium1.txt"))
	sudoku.infer_improved()
	sudoku.print_board()

	print "\n"

	sudoku = Sudoku(read_board("hw4-medium2.txt"))
	sudoku.infer_improved()
	sudoku.print_board()

	print "\n"

	sudoku = Sudoku(read_board("hw4-medium3.txt"))
	sudoku.infer_improved()
	sudoku.print_board()

	print "\n"

	sudoku = Sudoku(read_board("hw4-medium4.txt"))
	sudoku.infer_improved()
	sudoku.print_board()

def test_section_4():

	sudoku = Sudoku(read_board("hw4-hard1.txt"))
	sudoku.infer_with_guessing()
	sudoku.print_board()

	print "\n"

	sudoku = Sudoku(read_board("hw4-hard2.txt"))
	sudoku.infer_with_guessing()
	sudoku.print_board()

if __name__ == "__main__":
	print "Testing Sudoku Structure\n"
	test_section_1()
	print "\nTesting AC-3\n"
	test_section_2()
	print "\nTesting Improved AC-3\n"
	test_section_3()
	print "\nTesting AC-3 with Guessing\n"
	test_section_4()