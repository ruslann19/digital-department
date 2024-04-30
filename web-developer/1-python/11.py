def lists_sum(*args, unique=False):
    numbers = []
    for l in args:
        numbers += l
    
    if unique == True:
        numbers = list(set(numbers))

    return sum(numbers)

# -----------------------------------------------

# lists_sum([1, 1], [1], [1, 2, 3])

# lists_sum([1, 1, 1], [1, 1], unique=True)

# lists_sum([1, 1, 1], unique=False)

# lists_sum([1, 2, 1, 2])
