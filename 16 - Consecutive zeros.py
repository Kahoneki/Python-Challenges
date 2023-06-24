def consecutive_zeros(string):
    return len(max(string.split('1'), key=len))