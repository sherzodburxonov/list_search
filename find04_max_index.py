def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    n=0
    KATTASI=data[0]
    while n<len(data):
        if KATTASI<data[n]:
            KATTASI=data[n]
        n=n+1
    return data.index(KATTASI)
print(find_max_index([12, 2, 5, 2, 7, 9, 1]))
    
