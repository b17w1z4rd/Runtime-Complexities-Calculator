# -*- coding: utf-8 -*-
"""Runtime_Complexities_Calculation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b8ZV8F0TtV0ljuUlpQH7MO7Ht2VxTgbi
"""

import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]


def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time


def main():
    sizes = [100, 200, 300, 400, 500, 1000, 2000, 3000]
    results = {"Bubble Sort": [], "Merge Sort": []}

    for size in sizes:
        random_list = generate_random_list(size)

        bubble_sort_time = measure_time(bubble_sort, random_list.copy())
        merge_sort_time = measure_time(merge_sort, random_list.copy())

        results["Bubble Sort"].append((size, bubble_sort_time))
        results["Merge Sort"].append((size, merge_sort_time))

    print("Run-time complexities (in seconds):")
    for alg, times in results.items():
        print(f"\n{alg}:")
        for size, time_taken in times:
            print(f"Size {size}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()