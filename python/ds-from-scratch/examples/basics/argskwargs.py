import random


def arbitrary_args_printer(a, b, *args, **kwargs):
    print(f"Fixed args: {a}, {b}")
    print(f"Unnamed args: {args}")
    print(f"Named args: {kwargs}")


arbitrary_args_printer(1, 2, 3, 4, kw1="a", kw2="b")
arbitrary_args_printer(0, 1, 2)
arbitrary_args_printer(1, 2)


# It works the other way too: use a list to supply unnamed args and a dictionary to supply named args when
# calling a function
def three_arger(a, b, c):
    print(f"{a} {b} {c}")


three_arger(*[11, 22], **{"c": 55})


# Very useful to define higher-order functions
def doubler(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)

    return g


def sum_many(a, b, c, d=1, e=2):
    return a + b + c + d + e


res_1 = doubler(sum_many)(1, 1, c=1, d=2, e=2)
res_2 = doubler(sum_many)(2, 2, 2, 4, 4)
res_3 = doubler(random.random)()
