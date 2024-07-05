#!/usr/bin/python3
"""
this module contains a function that finds
a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    return _find_peak(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak(arr, low, high):
    """finds a peak in a list of unsorted integers"""
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr)
                                                   - 1 or arr[mid + 1]
                                                   <= arr[mid]):
        return arr[mid]
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return _find_peak(arr, low, mid - 1)
    else:
        return _find_peak(arr, mid + 1, high)
