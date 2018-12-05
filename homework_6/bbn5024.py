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
import random

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
        if n != 1:
            context = context[n-(n-1):] + (token, )

    return all_ngrams

class NgramModel(object):

    def __init__(self, n):

        self.n = n
        self.all_ngrams = {}

        # Used to increase efficiency of n = 1 models
        self.one_gram_dict = {}
        self.one_gram_set = set()
        self.needs_sort = False

    def update(self, sentence):
        
        tokens = tokenize(sentence)
        new_ngrams = ngrams(self.n, tokens)

        for context, token in new_ngrams:

            if self.n == 1:
                if token in self.one_gram_dict:
                    self.one_gram_dict[token] += 1
                else:
                    self.one_gram_dict[token] = 1
            else:
                if context in self.all_ngrams:
                    self.all_ngrams[context].append(token)
                else:
                    self.all_ngrams[context] = [token]

        if self.n == 1:
            self.needs_sort = True

    def prob(self, context, token):

        # If one gram, simply get probability from count of of tokens in dict
        if self.n == 1:
            return 1.0 * self.one_gram_dict[token] / sum(self.one_gram_dict.values())

        count = 0
        total = len(self.all_ngrams[context])
        
        for ngram in self.all_ngrams[context]:
            if token == ngram:
                count += 1

        return 1.0 * count / total

    def random_token(self, context):
        
        r = random.random()

        if self.n == 1 and self.needs_sort:
            self.one_gram_set = sorted(set(self.one_gram_dict.keys()))
            tokens = self.one_gram_set
            self.needs_sort = False
        elif self.n == 1:
            tokens = self.one_gram_set
        else:
            tokens = sorted(set(self.all_ngrams[context]))

        prob_sum = 0

        for token in tokens:
            p = self.prob(context, token)
            
            if p + prob_sum > r and r > prob_sum:
                return token
            prob_sum += p

    def random_text(self, token_count):

        context = tuple("<START>" for i in range(self.n - 1))
        random_tokens = []

        for i in range(token_count):
            r_token = self.random_token(context)
            random_tokens.append(r_token)

            if r_token == "<END>":
                context = tuple("<START>" for i in range(self.n - 1))
            elif self.n != 1:
                context = context[self.n-(self.n-1):] + (r_token, )
        
        return " ".join(random_tokens)

    def perplexity(self, sentence):
        
        tokens = tokenize(text)
        prev = "<START>"

def create_ngram_model(n, path):

    model = NgramModel(n)
    with open(path, "r") as f:
        for line in f:
            model.update(line)

    return model
    

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
5 hours.
"""

feedback_question_2 = """
No challenges.
"""

feedback_question_3 = """
Creating an n-grams model from scratch was fun.
"""
