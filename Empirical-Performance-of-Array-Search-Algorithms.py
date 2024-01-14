# Queens College
# Dicrete Structures CSCI 220
# Winter 2024
# Assignment 6 Empirical Performance of Search Algorithms
# Mikdad Abdullah
# Collaborated With Class


from random import randint
from matplotlib import pyplot as plt
import random
import pandas as pd
import time
import math


# [1] Define a function random_list(size) that  returns a sorted list of random numbers.
def random_list(n):
    numbers = [0] * n
    numbers[0] = randint(1, 10)
    for i in range(1, n):
        numbers[i] = numbers[i - 1] + randint(1, 10)
    return numbers


# [2] Define a function native_search(list, key) that wraps the built-in index function
def native_search(arr, key):
    return arr.index(key)


# [3] Define the following functions utilizing the code from the references provided.
# Ensure that signatures are consistent.:
def linear_search(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


def linear_search_sentinel(arr, key):
    n = len(arr)
    last = arr[n-1]
    arr[n-1] = key
    i = 0
    while arr[i] != key:
        i += 1
    arr[n-1] = last
    if i < n - 1 or arr[n-1] == key:
        return i
    else:
        return -1


def linear_search_recursive_rec(arr, key, size):
    if size == 0:
        return -1
    elif arr[size - 1] == key:
        return size - 1
    return linear_search_recursive_rec(arr, key, size - 1)

def linear_search_recursive(arr, key):
    return linear_search_recursive_rec(arr, key, len(arr) - 1)


def binary_search_iterative(arr, key):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binary_search_recursive_rec(arr, key, l, r):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive_rec(arr, key, l, mid - 1)
        else:
            return binary_search_recursive_rec(arr, key, mid + 1, r)
    else:
        return -1


def binary_search_recursive(arr, key):
    return binary_search_recursive_rec(arr, key, 0, len(arr) - 1)


def ternary_search_recursive_rec(arr, key, l, r):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            return ternary_search_recursive_rec(arr, key, l, mid1 - 1)
        elif key > arr[mid2]:
            return ternary_search_recursive_rec(arr, key, mid2 + 1, r)
        else:
            return ternary_search_recursive_rec(arr, key, mid1 + 1, mid2 - 1)
    return -1


def ternary_search_recursive(arr, key):
    return ternary_search_recursive_rec(arr, key, 0, len(arr) - 1)


def binary_search_randomized_rec(arr, key, l, r):
    if r >= l:
        mid = randint(l, r)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return binary_search_randomized_rec(arr, key, l, mid - 1)
        else:
            return binary_search_randomized_rec(arr, key, mid + 1, r)
    return -1


def binary_search_randomized(arr, key):
    return binary_search_randomized_rec(arr, key, 0, len(arr) - 1)


def binary_search_onesided(arr, key):
    n = len(arr)
    lg = int(math.log2(n - 1)) + 1
    pos = 0
    for i in range(lg - 1, -1, -1):
        if arr[pos] == key:
            return pos
        new_pos = pos | (1 << i)
        if new_pos < n and arr[new_pos] <= key:
            pos = new_pos
    return pos if arr[pos] == key else -1


def binary_search_better(arr, key):
    l, r = 0, len(arr) - 1
    while r-l > 1:
        m = l+(r-l)//2
        if arr[m] <= key:
            l = m
        else:
            r = m
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r
    return -1

# https://www.geeksforgeeks.org/ternary-search/
def ternary_search_iterative(arr, key):
    l = 0
    r = len(arr) - 1
    while r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            r = mid1 - 1
        elif key > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1


def ternary_search_randomized_rec(arr, key, l, r):
    if r >= l:
        mid1 = randint(l, (l + r) // 2)
        mid2 = randint((l + r) // 2, r)
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif arr[mid1] > key:
            return ternary_search_randomized_rec(arr, key, l, mid1 - 1) # first part
        elif arr[mid2] < key:
            return ternary_search_randomized_rec(arr, key, mid2 + 1, r)  # Third part
        else:
            return ternary_search_randomized_rec(arr, key, mid1 + 1, mid2 - 1) # the seocnd part
    return -1


def ternary_search_randomized(arr, key):
    return ternary_search_randomized_rec(arr, key, 0, len(arr) - 1)


def exponential_search(arr, key):
    if arr[0] == key:
        return 0
    n=len(arr)
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2
    return binary_search_recursive_rec(arr, key, i // 2, min(i, n - 1))



def jump_search(arr, key):
    n=len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[int(min(step, n) - 1)] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < key:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

    # If element is found
    if arr[int(prev)] == key:
        return prev

    return -1
# [4] Add code to verify that the current search determines the correct position
# [5] Add code to time each of the search functions
# [6] Add code to run each search multiple times for different random keys


# [7] Add code to plot the timings for the algorithms. See https://www.geeksforgeeks.org/matplotlib-tutorial/
def plot_times(dict_algs, sizes, trials, algs, file_name):
    alg_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for alg in algs:
        alg_num += 1
        d = dict_algs[alg.__name__]
        x_axis = [j + 0.05 * alg_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=alg.__name__)
    plt.legend()
    plt.title("Runtime of Algorithms")
    plt.xlabel("Size")
    plt.ylabel(f"Time for {trials} trials (ms)")
    plt.savefig(file_name)
    plt.show()


# [8] Add code to print the timings in a table
def print_times(dict_algs):
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_algs).T
    print(df)


# Use this code as a starting point for running the searches:
def run_algs(algs, sizes, trials):
    dict_algs = {}
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr = random_list(size)
            idx = random.randint(0, size - 1)
            key = arr[idx]
            for alg in algs:
                start_time = time.time()
                idx_found = alg(arr, key)
                end_time = time.time()
                if idx_found != idx:
                    print(alg.__name__, "wrong index found", arr, idx, idx_found)
                net_time = end_time - start_time
                dict_algs[alg.__name__][size] += 1000 * net_time
    return dict_algs

def fibonacci_search(arr, key):
    n = len(arr)
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1

    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while (fibM > 1):
        i = min(offset + fibMMm2, n - 1)
        if (arr[i] < key):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > key):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    if (fibMMm1 and arr[n - 1] == key):
        return n - 1
    return -1

#https://www.geeksforgeeks.org/interpolation-search/
def interpolation_search_rec(arr, key, l, r):
    if l == r:
        if arr[l] == key:
            return l
        else:
            return -1
    if l <= r and arr[l] <= key <= arr[r]:
        pos = l + int(((r - l) / (arr[r] - arr[l])) * (key - arr[l]))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            return interpolation_search_rec(arr, key, pos + 1, r)
        if arr[pos] > key:
            return interpolation_search_rec(arr, key, l, pos - 1)
    return -1

def interpolation_search(arr, key):
    return interpolation_search_rec(arr, key, 0, len(arr) - 1)

def main():
    sizes = [10, 100, 1000, 10000]
    searches = [native_search, linear_search, linear_search_sentinel,
                binary_search_iterative, binary_search_recursive, binary_search_randomized, binary_search_onesided, binary_search_better,
                ternary_search_iterative, ternary_search_recursive, ternary_search_randomized,
                exponential_search, jump_search,
                fibonacci_search, interpolation_search]
    trials = 1000
    dict_searches = run_algs(searches, sizes, trials)
    print_times(dict_searches)
    plot_times(dict_searches, sizes, trials, searches, "Assignment6.png")


if __name__ == "__main__":
    main()
