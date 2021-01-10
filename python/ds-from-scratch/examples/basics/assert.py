# Use assert to implement basic tests

assert 1 + 1 == 2, "One plus one equals two"


def smallest_item(lst):
    return min(lst)


assert smallest_item([0, 1, 2, 3, 4, 5, 6, 7]) == 0, "Smallest should be zero"


# Less common use of assert: check function arguments
def some_func(lst):
    assert lst, "Empty list has no smallest item"
    return min(lst)

