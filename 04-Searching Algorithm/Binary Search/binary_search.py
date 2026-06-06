def binarySearch(L,x):
    
    left = 0
    right = len(L)-1
    
    while left <= right:
        mid = int((left + right)/2) # (left+right)//2
        
        if L[mid] == x:
            return mid
        
        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1 
            
    return -1

L = [1,2,3,4,5,6,7,8,9]

position = binarySearch(L,3)

print(position)
        