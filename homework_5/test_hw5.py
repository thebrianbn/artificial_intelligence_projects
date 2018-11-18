from bbn5024 import *
from nose.tools import assert_equals, assert_not_equals
import os

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


def test_section_3():

	sf = SpamFilter("homework5_data/train/spam2", "homework5_data/train/ham2", 1e-5)
	assert_equals(sf.is_spam("homework5_data/train/spam/spam1"), True)
	assert_equals(sf.is_spam("homework5_data/train/spam/spam2"), True)

	assert_equals(sf.is_spam("homework5_data/train/ham/ham1"), False)
	assert_equals(sf.is_spam("homework5_data/train/ham/ham2"), False)

	spam_paths = os.listdir("homework5_data/train/spam")
	spam_paths = map(lambda x: "homework5_data/train/spam/" + x, spam_paths)
	ham_paths = os.listdir("homework5_data/train/ham")
	ham_paths = map(lambda x: "homework5_data/train/ham/" + x, ham_paths)

	spam_count = 0
	ham_count = 0
	for spam_path in spam_paths:
		spam_count += sf.is_spam(spam_path)
		#assert_equals(sf.is_spam(spam_path), True)

	for ham_path in ham_paths:
		if not sf.is_spam(ham_path):
			ham_count += 1
		#assert_equals(sf.is_spam(ham_path), False)

	print spam_count, ham_count


def test_section_4():

	sf = SpamFilter("homework5_data/train/spam", "homework5_data/train/ham", 1e-5)
	assert_equals(sf.most_indicative_spam(5), ['<a', '<input', '<html>',
		'<meta', '</head>'])
	assert_equals(sf.most_indicative_ham(5), ['Aug', 'ilug@linux.ie',
		'install', 'spam.', 'Group:'])

if __name__ == "__main__":
	test_section_1()
	test_section_2()
	test_section_3()
	test_section_4()