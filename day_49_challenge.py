# Create a program that implements the bubble sort algorithm

def bubble_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

arr = [12, 42, 3, 5, 92, 11]
bubble_sort(arr)
print(f"Sorted array is: {arr}")