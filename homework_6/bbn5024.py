############################################################
# CMPSC 442: Homework 6
############################################################

student_name = "Brian Nguyen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string
import re

############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    
    space = False
    tokens = []
    current = ""

    for char in text:
        if char in string.punctuation:
            if len(current) != 0:
                tokens.append(current)
            tokens.append(char)
            current = ""
        elif char.isspace():
            space = True
        elif space:
            space = False
            if len(current) != 0:
                tokens.append(current)
            current = char
        else:
            current += char
    if len(current) != 0:
        tokens.append(current)

    return tokens

def ngrams(n, tokens):

    all_ngrams = []
    tokens.append("<END>")
    context = tuple("<START>" for i in range(n - 1))
    
    for token in tokens:
        all_ngrams.append((context, token))
        if n == 1:
            continue
        else:
            context = context[n-(n-1):] + (token, )

    return all_ngrams

class NgramModel(object):

    def __init__(self, n):
        self.n = n

    def update(self, sentence):
        pass

    def prob(self, context, token):
        pass

    def random_token(self, context):
        pass

    def random_text(self, token_count):
        pass

    def perplexity(self, sentence):
        pass

def create_ngram_model(n, path):
    pass

############################################################
# Section 2: Feedback
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
