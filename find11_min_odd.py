def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    n=0
    kichkinasi=data[0]
    while n<len(data):
        if data[n]%2==1:
            if kichkinasi>data[n]:
                kichkinasi=data[n]
        n=n+1
    return kichkinasi
print(find_min_odd([12, 2, 5, 2, 7, 17, 1]))
