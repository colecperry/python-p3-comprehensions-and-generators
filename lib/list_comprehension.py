#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [n for n in num_list if n % 2 == 0]
    return even_nums

def make_exclamation(sentence_list):
    exclamation_strings = [(n + "!") for n in sentence_list]
    return exclamation_strings
                           