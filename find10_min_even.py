def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    n=0
    kichkinasi=data[0]
    while n<len(data):
        if data[n]%2==0:
            if kichkinasi>data[n]:
                kichkinasi=data[n]
        n=n+1
    return kichkinasi
print(find_min_even([12, 2, 5, 2, 7, 17, 1]))


