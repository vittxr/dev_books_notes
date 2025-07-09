# quick_sort: O(n log n), but in the worst case it can be O(n²), but the med is O(n log n)
# for example in an already sorted arr, quick_sort has O(n)!

# selection_sort: O(n²) -> because it uses two loop (the inner one to find the smallest

# merge_sort: O(n log n) -> Often, the way Quicksort and merge sort are implemented, if they’re both O(n log n) time, quicksort is faster. And quicksort is faster in practice because it hits the average case way more often than the worst case.


# the quicksort uses divide-and-conquer, spiting the arr in two parts: left with the values smaller than pivot and the right with the values bigger than pivot.


fn_exec_count = 0


def quicksort(arr: list[int]) -> list[int]:
    global fn_exec_count
    fn_exec_count += 1

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


arr = [1, 4, 6, 1, 2]
print(quicksort(arr))
print("fn_exec_count: ", fn_exec_count)
