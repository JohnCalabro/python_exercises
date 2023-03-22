def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    li = []
    for item in lst:
        t = type(item)
        li.append(t)
    for ty in li:
        if ty != list:
            return 'not a list so false'
            
            
    

        

