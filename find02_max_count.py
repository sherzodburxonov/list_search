def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    n=0
    i=0
    KATTASI=data[0]
    while n<len(data):
        if KATTASI<data[n]:
            KATTASI=data[n]
        n=n+1
    while n<len(data): 
        if KATTASI==data[n]:
            i=i+1      
        n=n+1
    return i
print(find_max_count([12, 2, 5, 2, 7, 12, 1]))
