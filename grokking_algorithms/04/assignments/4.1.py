# Write out the code for the earlier sum function.


def sum(lst: list[int]) -> int:
    r = 0
    for e in lst:
        r += e

    return r


print(sum([1, 4, 6]))  # 11
