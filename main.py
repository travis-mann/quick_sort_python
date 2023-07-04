#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: quicksort algorithm implementation"""


# --- metadata ---
__author__ = "Travis Mann"
__version__ = "1.0"
__maintainer__ = "Travis Mann"
__email__ = "tmann.eng@gmail.com"


# --- imports ---
from typing import List


# --- glob vars ---
comparisons = 0


# --- func ---
def choose_first_pivot(array: List[int], left_index: int, right_index: int) -> int:
    """
    purpose: select a pivot from the array for partitioning
    :return:
    """
    return left_index


def choose_last_pivot(array: List[int], left_index: int, right_index: int) -> int:
    """
    purpose: choose the last element as a pivot
    :return:
    """
    return right_index


def choose_median_pivot(array: List[int], left_index: int, right_index: int) -> int:
    """
    purpose: calculate the median element for the pivot
    :return:
    """
    length = right_index - left_index + 1

    # get idx of middle element
    if length % 2 == 0:
        middle_idx = length // 2 - 1 + left_index
    else:
        middle_idx = length // 2 + left_index

    # get index for median between 1st, middle and last elements
    element_idx_map = {array[left_index]: left_index,
                       array[middle_idx]: middle_idx,
                       array[right_index]: right_index}
    median = sorted([array[left_index], array[middle_idx], array[right_index]])[1]
    return element_idx_map[median]


def partition(array: List[int], left_index: int, right_index: int) -> int:
    """
    purpose: swap all elements in an array such that elements less than the pivot are to the left of it and elements
             greater are to the right. Assumes that a pre-processing step has already moved the pivot into the 1st
             position.
    """
    # get pivot
    pivot = array[left_index]

    # scan array to make necessary swaps
    pivot_boundary_index = left_index + 1
    for scan_index in range(left_index + 1, right_index + 1):
        if array[scan_index] < pivot:
            # swap current value before pivot boundary
            array[pivot_boundary_index], array[scan_index] = array[scan_index], array[pivot_boundary_index]
            pivot_boundary_index += 1

    # swap pivot into correct final location
    array[pivot_boundary_index - 1], array[left_index] = array[left_index], array[pivot_boundary_index - 1]
    return pivot_boundary_index - 1


def quick_sort(array: List[int], left_index: int, right_index: int, choose_pivot: callable) -> None:
    """
    purpose: sort the given array recursively in ascending order
    """
    # base case
    if right_index <= left_index:
        return

    # calculate number of comparisons for all recursive calls
    global comparisons
    # if left_index != 0 or right_index != len(array) - 1:
    comparisons += right_index - left_index

    # recursive calls
    pivot_index = choose_pivot(array, left_index, right_index)
    # preprocess array to swap pivot to the left index and partition
    array[pivot_index], array[left_index] = array[left_index], array[pivot_index]
    partitioned_pivot_index = partition(array, left_index, right_index)
    # sort half before pivot
    quick_sort(array, left_index, partitioned_pivot_index - 1, choose_pivot)
    # sort half after pivot
    quick_sort(array, partitioned_pivot_index + 1, right_index, choose_pivot)


# --- main ---
if __name__ == "__main__":
    # extract list of ints as str from example file
    with open('example_array.txt') as file:
        original_array = file.readlines()

    # convert strings to ints
    original_array = [int(number.replace('\n', '')) for number in original_array]
    # original_array = [4, 3, 2, 1]

    # count comparisons made for various choose pivot implementations
    for choose_pivot_func in [choose_first_pivot,  # 162085, correct
                              choose_last_pivot,  # 164123, correct
                              choose_median_pivot]:  # 138382, correct
        print(f'sorting with {choose_pivot_func.__name__}')
        array_copy = original_array[:]
        quick_sort(array_copy, 0, len(array_copy) - 1, choose_pivot_func)
        print(f'sorted_array: {array_copy}')
        print(f'comparisons: {comparisons}')

        # reset comparison count for next iteration
        comparisons = 0
