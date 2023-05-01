def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    n=0
    kichkinasi=data[0]
    while n<len(data):
        if kichkinasi>data[n]:
            kichkinasi=data[n]
        n=n+1
    return kichkinasi
print(find_min([12, 2, 5, 2, 7, 9, 1]))
    