from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals
import os
import random

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


def test_section_3():

	m = NgramModel(1)
	m.update("a b c d")
	m.update("a b a b")
	assert_equals(m.prob((), "a"), 0.3)
	assert_equals(m.prob((), "c"), 0.1)
	assert_equals(m.prob((), "<END>"), 0.2)

	m = NgramModel(2)
	m.update("a b c d")
	m.update("a b a b")
	assert_equals(m.prob(("<START>",), "a"), 1.0)
	assert_equals(m.prob(("b",), "c"), 0.3333333333333333)
	assert_equals(m.prob(("a",), "x"), 0.0)


def test_section_4():

	m = NgramModel(1)
	m.update("a b c d")
	m.update("a b a b")
	random.seed(1)
	assert_equals([m.random_token(()) for i in range(25)],
		['<END>', 'c', 'b', 'a', 'a', 'a', 'b', 'b', '<END>', '<END>', 'c',
		'a', 'b', '<END>', 'a', 'b', 'a', 'd', 'd', '<END>', '<END>', 'b', 'd', 'a', 'a'])

	m = NgramModel(2)
	m.update("a b c d")
	m.update("a b a b")
	random.seed(2)
	assert_equals([m.random_token(("<START>",)) for i in range(6)],
		['a', 'a', 'a', 'a', 'a', 'a'])
	assert_equals([m.random_token(("b",)) for i in range(6)],
		['c', '<END>', 'a', 'a', 'a', '<END>'])


def test_section_5():

	m = NgramModel(1)
	m.update("a b c d")
	m.update("a b a b")
	random.seed(1)
	assert_equals(m.random_text(13), '<END> c b a a a b b <END> <END> c a b')

	m = NgramModel(2)
	m.update("a b c d")
	m.update("a b a b")
	random.seed(2)
	assert_equals(m.random_text(15), 'a b <END> a b c d <END> a b a b a b c')


def test_section_6():

	m = create_ngram_model(1, "frankenstein.txt")
	print m.random_text(15)
	m = create_ngram_model(2, "frankenstein.txt")
	print m.random_text(15)
	m = create_ngram_model(3, "frankenstein.txt")
	print m.random_text(15)
	m = create_ngram_model(4, "frankenstein.txt")
	print m.random_text(15)

if __name__ == "__main__":

	test_section_1()
	test_section_2()
	test_section_3()
	test_section_4()
	test_section_5()
	test_section_6()
