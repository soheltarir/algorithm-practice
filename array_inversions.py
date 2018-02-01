"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted
then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
"""


def merge(first: list, second: list):
    merged = []
    inv_count = 0
    i_a, i_b = 0, 0
    while True:
        if i_a == len(first) and i_b == len(second):
            break
        elif i_a == len(first):
            merged.append(second[i_b])
            i_b += 1
        elif i_b == len(second):
            merged.append(first[i_a])
            i_a += 1
        elif first[i_a] < second[i_b]:
            merged.append(first[i_a])
            i_a += 1
        else:
            merged.append(second[i_b])
            i_b += 1
            inv_count += 1

    return merged, inv_count


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr, 0
    mid = int(len(arr)/2)
    first, inv_a = merge_sort(arr[:mid])
    second, inv_b = merge_sort(arr[mid:])
    merged_arr, inv_c = merge(first, second)
    return merged_arr, inv_a + inv_b + inv_c
