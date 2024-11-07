import random
import time
import copy

# Deterministic QuickSort (using the last element as the pivot)
def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized QuickSort (choosing a random pivot)
def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]  # Swap random pivot to the end
    return deterministic_partition(arr, low, high)

# Performance Analysis Function
def analyze_quick_sort():
    # Generate a large random array for testing
    array_size = 10000
    arr = [random.randint(0, 100000) for _ in range(array_size)]
    
    # Copy arrays for fair comparison
    arr_deterministic = copy.deepcopy(arr)
    arr_randomized = copy.deepcopy(arr)
    
    # Measure time for Deterministic QuickSort
    start_time = time.time()
    deterministic_quick_sort(arr_deterministic, 0, len(arr_deterministic) - 1)
    deterministic_time = time.time() - start_time

    # Measure time for Randomized QuickSort
    start_time = time.time()
    randomized_quick_sort(arr_randomized, 0, len(arr_randomized) - 1)
    randomized_time = time.time() - start_time
    
    # Display results
    print(f"Array size: {array_size}")
    print(f"Deterministic QuickSort time: {deterministic_time:.6f} seconds")
    print(f"Randomized QuickSort time: {randomized_time:.6f} seconds")
    print("Is deterministic sort correct?", arr_deterministic == sorted(arr))
    print("Is randomized sort correct?", arr_randomized == sorted(arr))

# Run the analysis
analyze_quick_sort()
