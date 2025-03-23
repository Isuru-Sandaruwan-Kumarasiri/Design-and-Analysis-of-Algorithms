def selectionSort(array,size):
    for i in range(size-1):
        min_index=i
        for j in range(i+1,size):
            if array[j]<array[min_index]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]


array=[34,56,23,4,23,8,29]
size=len(array)
selectionSort(array,size)
print(array)