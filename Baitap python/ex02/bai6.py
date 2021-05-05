def saddle_points(matrix):
    """
    A saddle point is an element which is greaterh thean or equal to every
    element in its row, it must be also less than or equal to every element
    in its column.
    """
    # check that matrix in input is a quadratic one.
    for curr in range(len(matrix) - 1):
        next = curr + 1
        if len(matrix[curr]) != len(matrix[next]):
            raise ValueError('Insert a valid matrix.')

    results = set()
    for index, row in enumerate(matrix):
        candidates = [(i, x) for i, x in enumerate(row) if x == max(row)]
        for i, candidate in candidates:
            column = [row[i] for row in matrix]
            if candidate == min(column):
                results |= {(index, i)}
    return results