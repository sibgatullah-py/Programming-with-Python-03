def secondLargest(l):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in l:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    print('second largest',second_largest)
    
    
def secondSmallest(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
            
    print('second smallest',second_smallest)
    
    
arr = [8, 2, 4, 1, 5, 7]
secondLargest(arr)
secondSmallest(arr)