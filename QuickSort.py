def partition(arr,low,high):
    
    i = (low-1)         # index of smaller element
    pivot = arr[high]   # pivot

    for j in range(low , high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i+1     # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Recursively sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr


arr = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(arr)

size = len(arr)

quickSort(arr, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(arr)