L = [3,6,10,1,7,2,5,9,4,8]

n = len(L)

def sSort1(L,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if L[j]< L[min_idx]:
                min_idx = j
                
        if min_idx != i:
                L[i], L[min_idx] = L[min_idx], L[i] # Simultaneous (Tuple) assignment
            
    print(L)


# Example 
arr = [8,2,4,1,5,7]

l = len(arr)

def eSort(arr,l):
    for i in range(0,l-1):
        min_idx = i
        
        for j in range(i+1,l): # traversing through the list and finding the minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i: # if the found minimum isn't same as i then i is second minimum 
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
            
    print(arr)

eSort(arr,l)
