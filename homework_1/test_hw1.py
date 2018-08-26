from bbn5024 import *
from nose.tools import assert_equals

def test_section_2():

    #assert_equals(extract_and_apply(

    assert_equals(concatenate([[1, 2], [3, 4]]), [1, 2, 3, 4])
    assert_equals(concatenate(["abc", (0, [0])]), ['a', 'b', 'c', 0, [0]])

    assert_equals(transpose([[1, 2, 3]]), [[1], [2], [3]])
    assert_equals(transpose([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

def test_section_3():

	assert_equals(copy("abc"), "abc")
	assert_equals(copy((1, 2, 3)), (1, 2, 3))

	assert_equals(all_but_last("abc"), "ab")
	assert_equals(all_but_last((1, 2, 3)), (1, 2))
	assert_equals(all_but_last(""), "")
	assert_equals(all_but_last([]), [])

	assert_equals(every_other([1, 2, 3, 4, 5]), [1, 3, 5])
	assert_equals(every_other("abcde"), "ace")
	assert_equals(every_other([1, 2, 3, 4, 5, 6]), [1, 3, 5])
	assert_equals(every_other("abcdef"), "ace")

def test_section_4():

	assert_equals(list(prefixes([1, 2, 3])), [[], [1], [1, 2], [1, 2, 3]])
	assert_equals(list(prefixes("abc")), ['', 'a', 'ab', 'abc'])

	assert_equals(list(suffixes([1, 2, 3])), [[1, 2, 3], [2, 3], [3], []])
	assert_equals(list(suffixes("abc")), ['abc', 'bc', 'c', ''])

	assert_equals(list(slices([1, 2, 3])), [[1], [1, 2], [1, 2, 3], [2], [2, 3],
		[3]])
	assert_equals(list(slices("abc")), ['a', 'ab', 'abc', 'b', 'bc', 'c'])

def test_section_5():

	assert_equals(normalize("This is an example."), "this is an example.")
	assert_equals(normalize("    EXTRA   SPACE     "), "extra space")

	assert_equals(no_vowels("This Is An Example."), 'Ths s n xmpl.')
	assert_equals(no_vowels("We love Python!"), 'W lv Pythn!')

	assert_equals(digits_to_words("Zip Code: 19104"), 'one nine one zero four')
	assert_equals(digits_to_words("Pi is 3.1415..."), 'three one four one five')

	assert_equals(to_mixed_case("to_mixed_case"), "toMixedCase")
	assert_equals(to_mixed_case("__EXAMPLE__NAME__"), "exampleName")

def test_section_6():

	p = Polynomial([(2, 1), (1, 0)])
	assert_equals(p.get_polynomial(), ((2, 1), (1, 0)))
	p = Polynomial(((2, 1), (1, 0)))
	assert_equals(p.get_polynomial(), ((2, 1), (1, 0)))

	q = -p
	assert_equals(q.get_polynomial(), ((-2, 1), (-1, 0)))

	p = Polynomial([(2, 1), (1, 0)])
	q = Polynomial([(4, 3), (3, 2)])
	r = p + q
	assert_equals(r.get_polynomial(), ((2, 1), (1, 0), (4, 3), (3, 2)))

	q = p - p
	assert_equals(q.get_polynomial(), ((2, 1), (1, 0), (-2, 1), (-1, 0)))

	q = Polynomial([(4, 3), (3, 2)])
	r = p - q
	assert_equals(r.get_polynomial(), ((2, 1), (1, 0), (-4, 3), (-3, 2)))

	q = p * p
	assert_equals(q.get_polynomial(), ((4, 2), (2, 1), (2, 1), (1, 0)))

	q = Polynomial([(4, 3), (3, 2)])
	r = p * q
	assert_equals(r.get_polynomial(), ((8, 4), (6, 3), (4, 3), (3, 2)))

	assert_equals([p(x) for x in range(5)], [1, 3, 5, 7, 9])

	q = -(p * p) + p
	assert_equals([q(x) for x in range(5)], [0, -6, -20, -42, -72])

	q = -p + (p * p)
	assert_equals(q.get_polynomial(), ((-2, 1), (-1, 0), (4, 2), (2, 1),
		(2, 1), (1, 0)))
	q.simplify()
	assert_equals(q.get_polynomial(), ((4, 2), (2, 1)))

	q = p - p
	assert_equals(q.get_polynomial(), ((2, 1), (1, 0), (-2, 1), (-1, 0)))
	q.simplify()
	assert_equals(q.get_polynomial(), ((0, 0),))

if __name__ == "__main__":
	print "Testing Assertions on Section 2"
	test_section_2()
	print "Testing Assertions on Section 3"
	test_section_3()
	print "Testing Assertions on Section 4"
	test_section_4()
	print "Testing Assertions on Section 5"
	test_section_5()
	print "Testing Assertions on Section 6"
	test_section_6()
