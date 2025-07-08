# Write a recursive function to count the number of items in a list.

# The goal is to minimize the array’s length, as recommended in the book: "When you’re writing a recursive function involving an array, the base case is often an empty array or an array with one element. If you’re stuck, try that first."
def recursive_sum(lst: list[int | float]) -> int | float:
    if len(lst) == 0:
        return 0

    return lst[0] + recursive_sum(lst[1:])


print(recursive_sum([1, 4, 6]))  # 11
