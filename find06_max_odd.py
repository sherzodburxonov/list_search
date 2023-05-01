def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    n=0
    KATTASI=data[0]
    while n<len(data):
        if data[n]%2==1:
            if KATTASI<data[n]:
                KATTASI=data[n]
        n=n+1
    return KATTASI
print(find_max_odd([12, 2, 5, 2, 7, 17, 1]))