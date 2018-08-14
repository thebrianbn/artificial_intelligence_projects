############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Brian Nguyen"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """

"""

python_concepts_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

python_concepts_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [x for x in seq for seq in seqs]

def transpose(matrix):
    pass

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    pass

def suffixes(seq):
    pass

def slices(seq):
    pass

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())

def no_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    return "".join([char for char in text if char.lower() not in vowels])

def digits_to_words(text):
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

    " ".join([digit_dict[char] for char in text if char in digit_dict])

def to_mixed_case(name):
    if "_" in name:
        temp = name.replace("_", " ").split()
        return temp

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        pass

    def get_polynomial(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    def simplify(self):
        pass

    def __str__(self):
        pass

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
