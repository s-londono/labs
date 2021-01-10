import re

# Search matches anywhere within the string. Match requires an exact match at the beginning of the string
re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),  # Split on a or b to ['c', 'r', 's']
    "R-D" == re.sub("[0-9]", "-", "R2D2")  # Replace digits with dashes
]

