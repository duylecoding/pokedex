import pandas as pd

def str_break(word):
    words = [x for x in word]
    for c in range(1, len(words)):
        if words[c].isupper():
            words[c] = ' ' + words[c]
    final = ''.join(words).split(' ')
    return final

def bracket_strings(word):
    words = [x for x in word]
    for char in range(1, len(words)):
        if words[char].isupper():
            words[char] = ' ' + words[char]
    final = ''.join(words).split(' ')
    length = len(words)
    if length > 1:
        final.insert(1, '(')
        final.append(')')
    return ' '.join(final)

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')