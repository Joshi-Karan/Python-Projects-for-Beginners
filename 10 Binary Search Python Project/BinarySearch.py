''' 
We will search for worst case
The result:
    Binary search time: 0.0
    Naive search time: 0.002201557159423828
'''
from time import time

def binary_search_time(arr, val: int, start = None, end = None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return binary_search_time(arr, val, start, mid-1)
    else:
        return binary_search_time(arr, val, mid+1, end)


def naive_search_time(arr: list, end: int, val: int) -> None:
    for i in range(end):
        if arr[i] == val:
            return True
    return False


if __name__ == "__main__":
    arr = []
    for i in range(10000):
        arr.append(i)
    val = 9999
    start = time()
    if binary_search_time(arr, val, 0, 9999):
        end = time()
        print('Binary search time:', end - start)
    start = time()
    if naive_search_time(arr, 10000, val):
        end = time()
        print('Naive search time:', end - start)
