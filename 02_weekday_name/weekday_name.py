def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weeks = {
        1: 'Sunday', 
        2: 'Monday', 
        3: 'Tuesday', 
        4: 'Wednesday', 
        5: 'Thursday',
        6: 'Friday', 
        7: 'Saturday'
    }

    if (day_of_week in range(1,7)):
        return weeks[day_of_week]
    else:
        return None
    

    # if else in python

#     In [296]: {num: num * num for num in range(1,10)}
# Out[296]: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}