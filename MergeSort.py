def mergeSort(arr):
    print(arr)
    if len(arr)==1:
        return arr
        
    mid=len(arr)//2    
    L=arr[:mid]
    R=arr[mid:]

    mergeSort(L)
    mergeSort(R)
    merge(arr,L,R)
    return arr

def merge(arr,L,R):
   
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    # checking if any element was left
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1

    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

    return arr
  










if __name__=="__main__":

  arr =[23,4,67,34,89,21,11,9]
  print("Given array is :",arr)
  mergeSort(arr)
  print("Sorted array is :",arr)