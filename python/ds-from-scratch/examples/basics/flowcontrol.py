# Shortcut for if-else statements
parity = "even" if 4 % 2 == 0 else "odd"

# Truthiness. Python lets you use any value where it expects a boolean
# Falsy values:
# - False
# - None
# - []
# - {}
# - ""
# - set()
# - 0
# - 0.0

true_equals_false = True == False  # This is false

# Very short way to get first char of string or if the string is empty, get empty string
s = "abc"
first_char = s and s[0]

# Same for ints and 0
x = 20
safe_x = x or 0

# Functions all and any. All checks that all elements are truthy, any checks that at least an element is truthy
all([True, "aaa", 34, {2, 3}, ["a"]])
any([0, 0, 0, 0, 0, 0, 0, 3, 0, 0])

