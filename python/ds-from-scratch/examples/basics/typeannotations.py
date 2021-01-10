# The typing module contains many types, such as Dict, Iterable, Tuple to be used in type annotations
from typing import Union, List, Optional, Dict, Iterable, Tuple, Callable


# The following function is valid in Python 3.6. However, this annotations do nothing. They are just for
# documentation purposes and to be used with external tools such as mypy. Morover, enhances autocomplete of IDEs
def add(a: int, b: int) -> int:
    return a + b


s1 = add(4, 2)
s2 = add("a", "b")


# The use of Union here, means that the second argument can be either a str, int, float or bool
def ugly_function(val: List[int], operation: Union[str, int, float, bool]) -> str:
    return str(val) + " " + str(operation)


# Inline type hints:
# The following means that  a_var is  allowed to be either a float or None
a_var: Optional[float] = None
b_var: List[int] = []

# Keys are strings, values are ints
a_dict: Dict[str, int] = {"a": 1}

# Lists and generators are both iterable
an_iter: Iterable[int] = (x for x in [1, 2, 3, 4, 5])

# Tuples specify the type of each element
a_tuple: Tuple[int, str, bool] = (25, "twentyfive", True)

# Callable can be used to annotate function variables. Here, a function that expects an int and a float
# as arguments and returns a string
a_function = Callable[[int, float], str]

# Type annotations are just Python objects, so they can be assigned to variables
Number = Union[int, float]
Numbers = List[Number]

some_nums: Numbers = [1, 2, 2.3, 4.1, 0]





