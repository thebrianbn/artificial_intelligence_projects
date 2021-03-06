############################################################
# CMPSC442: Homework 5
############################################################
student_name = "Brian Nguyen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import email
from math import log, exp
import os


############################################################
# Section 1: Spam Filter
############################################################

def load_tokens(email_path):

    tokens = []
    
    with open(email_path, "r") as f:
        e = email.message_from_file(f)
    for line in email.iterators.body_line_iterator(e):
        tokens += line.split()

    return tokens

def get_token_counts(email_paths):

    token_dict = {}

    # Get counts of each token
    for path in email_paths:
        tokens = load_tokens(path)
        for token in tokens:
            if token in token_dict:
                token_dict[token] += 1
            else:
                token_dict[token] = 1

    return token_dict

def log_probs(email_paths, smoothing):

    token_dict = get_token_counts(email_paths)

    token_log_probs = {}

    total_counts = sum(token_dict.values())
    token_length = len(token_dict)

    # Calculate log probabilities for each token
    for token, count in token_dict.items():
        token_log_probs[token] = log((count + smoothing) /
            ((total_counts) + (smoothing * (token_length + 1))) * 1.0)

    # Log probability for unknown token
    token_log_probs["<UNK>"] = log(smoothing / (total_counts +
        (smoothing * (token_length + 1))) * 1.0)

    return token_log_probs


class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):

        spam_paths = os.listdir(spam_dir)
        spam_paths = map(lambda x: spam_dir + "/" + x, spam_paths)
        ham_paths = os.listdir(ham_dir)
        ham_paths = map(lambda x: ham_dir + "/" + x, ham_paths)

        self.spam_prob = log(len(spam_paths) / (len(spam_paths) + len(ham_paths) * 1.0))
        self.ham_prob = log(len(ham_paths) / (len(spam_paths) + len(ham_paths) * 1.0))

        self.spam_logs = log_probs(spam_paths, smoothing)
        self.ham_logs = log_probs(ham_paths, smoothing)   
    
    def is_spam(self, email_path):

        token_counts = get_token_counts([email_path])
        
        spam_product = 0
        ham_product = 0
        for token, count in token_counts.items():
            # Spam
            if token in self.spam_logs:
                spam_product += self.spam_logs[token]
            else:
                spam_product += self.spam_logs["<UNK>"]
            
            # Ham
            if token in self.ham_logs:
                ham_product += self.ham_logs[token]
            else:
                ham_product += self.ham_logs["<UNK>"]

        doc_spam_prob = self.spam_prob + spam_product
        doc_ham_prob = self.ham_prob + ham_product

        return doc_spam_prob > doc_ham_prob

    def most_indicative_spam(self, n):

        indicative_tuple = []
        
        for token, log_prob in self.ham_logs.items():
            if token in self.spam_logs:
                denominator = exp(1) ** self.ham_logs[token] + exp(1) ** self.spam_logs[token]
            else:
                denominator = exp(1) ** self.ham_logs[token] + exp(1) ** self.spam_logs["<UNK>"]

            indicative_tuple.append((token, log_prob - log(denominator)))

        indicative_tuple.sort(key=lambda x: x[1], reverse=False)

        return list(map(lambda x: x[0], indicative_tuple))[:n]

    def most_indicative_ham(self, n):
        
        indicative_tuple = []
        
        for token, log_prob in self.spam_logs.items():
            if token in self.ham_logs:
                denominator = exp(1) ** self.spam_logs[token] + exp(1) ** self.ham_logs[token]
            else:
                denominator = exp(1) ** self.spam_logs[token] + exp(1) ** self.ham_logs["<UNK>"]

            indicative_tuple.append((token, log_prob - log(denominator)))

        indicative_tuple.sort(key=lambda x: x[1], reverse=False)

        return list(map(lambda x: x[0], indicative_tuple))[:n]
        

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
6 hours.
"""

feedback_question_2 = """
Classifying documents was tricky at first.
"""

feedback_question_3 = """
Classifying documents was enjoyable. I would make the forumlas more clear
since doing them in log space was tricky.
"""
