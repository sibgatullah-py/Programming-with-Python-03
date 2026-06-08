L = [3,6,10,1,7,2,5,9,4,8]

n = len(L)

def sSort1(L,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if L[j]< L[min_idx]:
                min_idx = j
                
        if min_idx != i:
                L[i], L[min_idx] = L[min_idx], L[i]   
            
    print(L)


def sSort2(L,n):
    for i in range(n-1):
        min = L[i]
        if L[i] > L[i+1]:
            L[i] = L[i+1]
            L[i+1] = min
        
        i+=1
        
    print(L)
    
sSort2(L,n)