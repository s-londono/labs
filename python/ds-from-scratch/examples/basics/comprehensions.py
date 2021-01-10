# Pythonic way to transform and filter lists

even_squares = [x * x for x in range(0, 50) if x % 2 == 0]

# Turn lists into dictionaries or sets
square_odd_dict = {x: x * x for x in range(20) if x % 2 == 1}
square_pair_set = {x for x in range(20) if x % 2 == 0}

zeros = [0 for _ in range(25)]

# List comprehensions can include multiple fors. Later fors can use values of previous fors
pairs = [(x, y) for x in range(10) for y in range(x + 1, 10)]

