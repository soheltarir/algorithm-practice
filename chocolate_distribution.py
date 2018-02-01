"""
Given an array of n integers where each value represents number of chocolates in a packet. Each packet can have variable
 number of chocolates. There are m students, the task is to distribute chocolate packets such that :

* Each student gets one packet.
* The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates
given to the students is minimum.
"""
from sys import maxsize


def find_min_diff(arr: list, m: int):
    if not len(arr) or not m:
        return 0
    if len(arr) < m:
        return -1
    arr.sort()
    min_diff = maxsize
    # Find the subarray of size m such that the difference between the last and first elements is minimum
    first, last = 0, 0
    index = 0
    while index + m - 1 < len(arr):
        diff = arr[index + m - 1] - arr[index]
        if diff < min_diff:
            min_diff = diff
            first = index
            last = index + m - 1
        index += 1
    return arr[last] - arr[first]


if __name__ == "__main__":
    array = [12, 4, 7, 9, 2, 23, 25, 41,
             30, 40, 28, 42, 30, 44, 48,
             43, 50]
    num_of_students = 7
    print("Minimum difference is {0}".format(find_min_diff(array, num_of_students)))
