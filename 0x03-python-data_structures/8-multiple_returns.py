#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return len(sentence), None
    if sentence:
        return len(sentence), sentence[0]