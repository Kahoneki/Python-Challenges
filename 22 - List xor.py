#My solution
def list_xor(n, list1, list2):
    return False if (n in list1 and n in list2) or (n not in list1 and n not in list2) else True

#Best solution
def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)