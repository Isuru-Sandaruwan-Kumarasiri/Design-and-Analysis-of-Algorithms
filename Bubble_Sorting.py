def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(not swapped)
        if not swapped:
            return
# arr = [64, 34, 25, 12, 22, 11, 90]   
arr = [ 11,12,13,14]  # thease two arrays are being used to check  why is used not swappped variable. 
bubbleSort(arr)
print("Sorted array is:", arr)