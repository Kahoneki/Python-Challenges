uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def capital_indexes(string):
    return [i for i,char in enumerate(string) if char in uppercase]