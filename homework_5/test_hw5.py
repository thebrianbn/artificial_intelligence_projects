from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals

def test_section_1():

	assert_equals(load_tokens("homework5_data/train/ham/ham1")[200:204],
		['of', 'my', 'outstanding', 'mail'])
	assert_equals(load_tokens("homework5_data/train/ham/ham2")[110:114],
		['for', 'Preferences', '-', "didn't"])
	assert_equals(load_tokens("homework5_data/train/spam/spam1")[1:5],
		['You', 'are', 'receiving', 'this'])
	assert_equals(load_tokens("homework5_data/train/spam/spam2")[:4],
		['<html>', '<body>', '<center>', '<h3>'])

def test_section_2():

	paths = ["homework5_data/train/ham/ham%d" % i for i in range(1, 11)]
	p = log_probs(paths, 1e-5)
	assert_equals(p["the"], -3.6080194731874062)
	assert_equals(p["line"], -4.272995709320345)

	paths = ["homework5_data/train/spam/spam%d" % i for i in range(1, 11)]
	p = log_probs(paths, 1e-5)
	assert_equals(p["Credit"], -5.837004641921745)
	assert_equals(p["<UNK>"], -20.34566288044584)
	

if __name__ == "__main__":
	test_section_1()
	test_section_2()