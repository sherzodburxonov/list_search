def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    n=0
    KATTASI=data[0]
    while n<len(data):
        if KATTASI<data[n]:
            KATTASI=data[n]
        n=n+1
    return KATTASI
print(find_max([12, 2, 5, 2, 7, 9, 1]))
    