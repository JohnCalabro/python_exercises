def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    liA = []
    liB = []
    for hob in a:
        # print(qual)
        liA.append(hob)
    # print(li[2])
    hobbiesA = liA[2]
    # print(hobbiesA)

    for hob in b:
        
        liB.append(hob)
   
    hobbiesB = liB[2]

    hobSetA = set(hobbiesA)
    hobSetB = set(hobbiesB)
    print(hobSetA,hobSetB)
    in_common_set = hobSetA.intersection(hobSetB)
    if len(in_common_set) != 0:
        return True
    else:
        return False
    



# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)




    # for h in hobbiesB:
    #     print(hobbiesA)
    #     if h in hobbiesA:
    #         return True
    # return False
        # elif h not in hobbiesA:
        #     return False
        
        
        
    #     if h in hobbiesA:
    #         return True
    #     else:
    #         return False

# So we convert the lists into sets and then create a new set by combining the given sets. 
# If they have some common elements then the new set will not be empty.Dec 23, 2019



friend_date(('Elmo', 5, ['hugging', 'being nice']),('Sauron', 5000, ['killing hobbits', 'chess']))

# friend_date(('Gandalf', 10000, ['waving wands', 'chess']),('Sauron', 5000, ['killing hobbits', 'chess']))










