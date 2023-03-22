def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)





def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    if fn == is_even:
        for itm in lst:
            li_one = [itm for itm in lst if is_even(itm)]
            li_two = [itm for itm in lst if not is_even(itm)]
            # print(li_one)
            print(li_two)
        return [li_one, li_two]
    else:
        for itm in lst:
            li_one = [itm for itm in lst if is_string(itm)]
            li_two = [itm for itm in lst if not is_string(itm)]
            print(li_one,li_two)
        return[li_one, li_two]





#             In [48]: isinstance('hi',str)
# Out[48]: True


    
    
    
    # return [li_one, li_two]
    
    # if fn == is_string:
    #     print('is string')
