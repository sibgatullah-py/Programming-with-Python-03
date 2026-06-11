def bubble(l):
    n = len(l)
    
    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                
if __name__ == "__main__":
    l = [6,1,4,9,2]
    bubble(l)
    print(l)