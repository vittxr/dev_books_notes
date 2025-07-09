# Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

fn_exec_count = 0


# this fn implements the logic of divide and conquer as asked in question, reducing the size of the array, but with this fn is not possible return the target element index because we modify the array! so the proper solution for binary search is keep the initial arr immutable!
# the answer of this question is: The base case for binary search occurs when the array has only one element. If that element matches the one you’re looking for, you’ve found it! Otherwise, it isn’t in the array.
def recursive_binary_search(arr: list[int], target: int) -> int:
    global fn_exec_count
    fn_exec_count += 1

    low = 0
    high = len(arr)
    mid = int(low + (high - low) / 2)
    print(f"checking arr[{mid}] = {arr[mid]}")

    if arr[mid] == target:
        print("found element in idx", mid)
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr[:mid], target)
    else:
        return recursive_binary_search(arr[mid:], target)


# this returns target element index! (since the array size is not reduced)
def recursive_binary_search2(
    arr: list[int], target: int, low: int = 0, high: int | None = None
) -> int:
    global fn_exec_count
    fn_exec_count += 1

    if high is None:
        high = len(arr) - 1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        # Recursive case: search left half
        return recursive_binary_search2(arr, target, low, mid - 1)
    else:
        # Recursive case: search right half
        return recursive_binary_search2(arr, target, mid + 1, high)


arr = [
    1,
    40,
    60,
    80,
    90,
    200,
    400,
    500,
    1000,
    1500,
    2000,
    2500,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
]
recursive_binary_search(arr, 400)
print("exec count - O(log n): ", fn_exec_count, " where arr length is ", len(arr))
