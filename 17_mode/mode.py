def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    new_li = []
    val_li = []
    for n in nums:
        freq = nums.count(n)
        dnry = {freq:n}
        new_li.append(dnry)
    
    
    for item in new_li:
        print(item, item.get(max(item)))
        items = item.get(max(item))
        
    return items
    
    


 