def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    out = 1

    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            out *= nums[i]
        if nums[i] % 2 != 0 and nums[i] % 2 == 0 not in nums:
            return 1
    return out
    

    
   