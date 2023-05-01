def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    n=0
    KATTASI=data[0]
    kichkinasi=data[0]
    while n<len(data):
        if KATTASI<data[n]:
            KATTASI=data[n]
        if kichkinasi>data[n]:
            kichkinasi=data[n]
        n=n+1
    return kichkinasi+KATTASI
print(find_max_min_sum([12, 2, 5, 2, 7, 9, 1]))

