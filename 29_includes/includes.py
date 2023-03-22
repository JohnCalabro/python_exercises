def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    print(start)
    if sought in collection and start == None:
        return True
    elif start != None and type(collection) != set:
        
        lngth = len(collection)
        print(lngth)

        cut = collection[start:lngth]
        print(cut)
        return sought in cut
    elif type(collection) == dict:
        print('coolio')
        start=None
        val_list = collection.values()
        print(val_list)
        return sought in val_list
    elif type(collection) == set:
        start=None
        print('ok')
        col_list = list(collection)
        return sought in col_list
    
        
        

