def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    
    already_visited = set()
    print(already_visited)

    for i in nums:
        difference = goal - i  #for each i in nums, subtract i from the difference
        print(difference)
        print(already_visited)

        if difference in already_visited:   
            return (difference, i)    #< -it's not so skip this at first

        already_visited.add(i)   # has no effect if element is already present
        ^ now add each i to the new set()   # now it will be filled go back to if difference above
    return ()   # other wise return empty set?

    # ^ I understand (kind of...)

    # Help on method_descriptor:

# add(...)
#     Add an element to a set.
    
#     This has no effect if the element is already present.
# (END)

    


    


#     In [40]: nums
# Out[40]: [1, 2, 2, 10]

# In [41]: nums[0:2]
# Out[41]: [1, 2]

    # Lst[ Initial : End : IndexJump ]

    
# %run sum_pairs.py

# sum_pairs([1,2,2,10],4)