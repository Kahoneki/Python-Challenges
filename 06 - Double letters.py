def double_letters(string):
    return any([a == b for a,b in zip(string, string[1:])])