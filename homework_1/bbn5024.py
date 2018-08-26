############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Brian Nguyen"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Python being strongly typed means that variables cannot be implicitly coerced
to unrelated types. For example, the following would not be possible (would
result in TypeError):

    temp = "3 + 21 = " + 24

However, with an explicit type conversion, there would be no error.

    temp = "3 + 21 = " + str(24)

Python being dynamically typed means that variable names are not bound to a
type. They are only bound to objects. This means that variable names can be
bound to different objects of different types at different parts of a program.
For example this is allowed in Python, but would not be allowed in a
statically typed language:

    temp = 3
    temp = "3"
"""

python_concepts_question_2 = """
The problem is that lists are mutable objects, resulting in issues with having
a list when being used as a key to a dictionary object. When a key is hashed in
a dictionary, it gets a unique hash to that key. If that key is changed, the
hash changes, resulting in the inability to retrieve the value for that key. 
A solution to this problem would be to use tuples as the coordinates, as
tuples are immutable objects.
"""

python_concepts_question_3 = """
The second version is better. Since strings are immutable, the first version
is allocating memory for each new concatentation of strings, resulting in a
new string, not a modified one, each time. The second method allocates
memory for only one new string and joins all of the strings in the iterator.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    """ Extracts the elements of a list l satisfying a boolean predicate p ,
    applies a function f to each such element, and returns the result. """

    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    """ Returns a list containing the concatenation of the elements of the
    input sequences. """

    return [x for seq in seqs for x in seq]

def transpose(matrix):
    """ Returns the transpose of the input matrix, which is represented as a
    list of lists. """

    # Assumption of rows all having same length and is not empty
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    """ Returns a new sequence containing the same elements as the input
    sequence. """

    return seq[:]

def all_but_last(seq):
    """ Returns a new sequence containing all but the last element of the
    input sequence. """

    return seq[:-1]

def every_other(seq):
    """ Returns a new sequence containing every other element of the input
    sequence, starting with the first. """

    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    """ Yields all prefixes of input sequence. """

    for x in range(len(seq) + 1):
        yield seq[:x]

def suffixes(seq):
    """ Yields all suffixes of input sequence. """

    for x in range(len(seq) + 1):
        yield seq[x:]

def slices(seq):
    """ Yields all non-empty slices of the input sequence. """

    for x in range(0, len(seq)):
        for y in range(x + 1, len(seq) + 1):
            yield seq[x:y]

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    """ Returns a normalized version of the input string, in which all words
    have been converted to lowercase and are separated by a single space. """

    return " ".join(text.lower().split())

def no_vowels(text):
    """ Removes all vowels from the input string and returns the result. """

    vowels = ["a", "e", "i", "o", "u"]
    return "".join([char for char in text if char.lower() not in vowels])

def digits_to_words(text):
    """ Extracts all digits from the input string, spells them out as lowercase
    English words, and returns a new string in which they are each separated by
    a single space. """

    digit_dict = {"0": "zero",
                  "1": "one",
                  "2": "two",
                  "3": "three",
                  "4": "four",
                  "5": "five",
                  "6": "six",
                  "7": "seven",
                  "8": "eight",
                  "9": "nine"}

    return " ".join([digit_dict[char] for char in text if char in digit_dict])

def to_mixed_case(name):
    """ Converts a variable name from underscore to mixed case. """

    name = name.replace("_", " ").lower().split()
    name[1:] = map(lambda x: x[0].upper() + x[1:], name[1:])
    return "".join(name)

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):
    """ Class supporting basic arithmetic, simplification, evaluation, and
    pretty-printing of polynomials. """

    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        return Polynomial(map(lambda x: (-x[0], x[1]), self.polynomial))

    def __add__(self, other):
        return Polynomial(self.polynomial + other.get_polynomial())

    def __sub__(self, other):
        return Polynomial(self.polynomial + (-other).get_polynomial())

    def __mul__(self, other):
        new_poly = []
        for pair1 in self.polynomial:
            for pair2 in other.get_polynomial():
                new_poly.append((pair1[0] * pair2[0], pair1[1] + pair2[1]))
        return Polynomial(new_poly)

    def __call__(self, x):
        return sum((pair[0] * x ** pair[1]) for pair in self.polynomial)

    def simplify(self):
        new_poly = []

        # Combine terms with common power
        for pair1 in self.polynomial:
            for x in range(len(new_poly)):
                if pair1[1] == new_poly[x][1]:
                    new_poly[x] = (pair1[0] + new_poly[x][0], pair1[1])
                    break
            else:
                new_poly.append(pair1)

        # Remove terms with coefficient of 0
        for pair in new_poly:
            if pair[0] == 0:
                new_poly.remove(pair)

        # Sort based on power
        new_poly.sort(key=lambda x: x[1], reverse=True)

        self.polynomial = tuple(new_poly)

    def __str__(self):
        poly_str = []
        first = True
        for pair in self.polynomial:
            if not first:  # Throw away sign and append operator if not first
                if pair[0] < 0:
                    poly_str.append("-")
                else:
                    poly_str.append("+")
                pair = (abs(pair[0]), pair[1])
            if pair[0] == 1 or pair[0] == -1:  # Throw away 1s
                if pair[0] == 1:
                    sign = ""
                else:
                    sign = "-"
                if pair[1] == 0:
                    poly_str.append(str(pair[0]))
                elif pair[1] == 1:
                    poly_str.append("%sx" % sign)
                else:
                    poly_str.append("%sx^%d" % (sign, pair[1]))
            else:
                if pair[1] == 0:
                    poly_str.append(str(pair[0]))
                elif pair[1] == 1:
                    poly_str.append("%dx" % pair[0])
                else:
                    poly_str.append("%dx^%d" % (pair[0], pair[1]))
            first = False

        return " ".join(poly_str)

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
I spent approximately 3.5 hours.
"""

feedback_question_2 = """
The Polynomial section was the most challenging. The other sections were
pretty straightforward. There were no significant stumbling blocks.
"""

feedback_question_3 = """
I enjoyed that I learned more than I already knew about Python. It makes me
critically think about efficiency of algorithms, list manipulation, and
other important aspects of artificial intelligence.
"""
