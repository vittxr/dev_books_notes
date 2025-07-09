# Write a recursive function to find the maximum number in a list.


def find(lst: list[int]) -> int:
    highv = 0

    for e in lst:
        if e > highv:
            highv = e

    return highv


def recursive_find(lst: list[int]) -> int:
    if len(lst) == 1:
        return lst[0]
    else:
        m = recursive_find(lst[1:])
        return m if m > lst[0] else lst[0]


print(find([1, 52, 50]))
print(recursive_find([1, 52, 50]))
