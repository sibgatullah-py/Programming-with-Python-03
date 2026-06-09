def find(l):
    n = len(l)
    largest = 0
    smallest = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if l[j]<l[smallest]:
                smallest = j
            if l[j]>l[largest]:
                largest = j
                
    print(f"Largest: {l[largest]} Smallest:{l[smallest]}")
    
L = [3,6,10,1,7,2,5,9,4,8]

find(L)