#Original Implementation
def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        for char in string1:
            if sum([char == i for i in string1]) != sum(char == i for i in string2):
                return False
        return True
    
#Alternatively, after learning about the sorted() function:
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)