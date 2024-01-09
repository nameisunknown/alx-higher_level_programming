#!/usr/bin/python3

def multiple_returns(sentence):
    tupl = ()
    counter = 0
    for alphab in sentence:
        counter += 1
    tupl = (counter, sentence[0])
    return tupl
