n = 100 # since the code has nth list as variable space so the space complexity is O(n)
even = [False] * (n+1) # lsit of n+1 space
for i in range(0, n+1,2):
    even[i] = True