from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals
import os

def test_section_1():

	assert_equals(tokenize("  This is an example.  "), ['This', 'is', 'an', 'example', '.'])
	assert_equals(tokenize("'Medium-rare,' she said."), ["'", 'Medium', '-', 'rare', ',', "'",'she', 'said', '.'])


def test_section_2():

	assert_equals(ngrams(1, ["a", "b", "c"]), [((), 'a'), ((), 'b'),
		((), 'c'), ((), '<END>')])
	assert_equals(ngrams(2, ["a", "b", "c"]), [(('<START>',), 'a'),
		(('a',), 'b'), (('b',), 'c'), (('c',), '<END>')])
	assert_equals(ngrams(3, ["a", "b", "c"]), [(('<START>', '<START>'), 'a'),
		(('<START>', 'a'), 'b'), (('a', 'b'), 'c'), (('b', 'c'), '<END>')])


if __name__ == "__main__":

	test_section_1()
	test_section_2()
