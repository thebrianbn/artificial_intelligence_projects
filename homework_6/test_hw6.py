from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals
import os

def test_section_1():

	assert_equals(tokenize("  This is an example.  "), ['This', 'is', 'an', 'example', '.'])
	assert_equals(tokenize("'Medium-rare,' she said."), ["'", 'Medium', '-', 'rare', ',', "'",'she', 'said', '.'])


if __name__ == "__main__":

	test_section_1()