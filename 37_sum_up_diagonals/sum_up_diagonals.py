
m1 = [[1,2],
      [30,40],
]

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]




def sum_up_diagonals(matrix):

    
    row_1 = matrix[0]
    row_2 = matrix[1]
    sum_1 = row_1[-1] + row_2[-2]
    sum_2 = row_1[-2] + row_2[-1]
    return sum_1 + sum_2

# can get first to work

    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
  

 