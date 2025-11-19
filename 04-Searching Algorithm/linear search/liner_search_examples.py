# time complexity of linear search is is O(n) and space complexity of linear search is O(1)

def linear_search_one(L,x):
    n = len(L)
    i = 0
    
    while i < n:
        if L[i] == x:
            return i
        
        i += 1
        
    i = -1
    
    return i

#=============================================================

def linear_search_two(L,x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return -1