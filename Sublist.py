"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because its memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if len(list_one) == len(list_two):
        return UNEQUAL
    list_one = "  ".join(map(lambda x: str(x), list_one))
    list_two = "  ".join(map(lambda x: str(x), list_two))
    if list_one in list_two:
        return SUBLIST
    if list_two in list_one:
        return SUPERLIST
    return UNEQUAL
