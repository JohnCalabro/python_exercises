def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    print(type(num1_str), type(num2_str))
    freq = [num1_str.count(lett) for lett in num1_str]
    freq2 = [num2_str.count(lett) for lett in num2_str]
    return freq == freq2