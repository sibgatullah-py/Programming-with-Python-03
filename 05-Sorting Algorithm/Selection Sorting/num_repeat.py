def repeat(l):
    n = len(l)
    checked = []
    for i in range(1,n):
        
        if l[i] in checked:
            continue
        
        count = 0
        for j in range(1,n):
            if l[j] == l[i]:
                count += 1
                
        print(f"{l[i]} repeated {count} times")
        
        checked.append(l[i])
        
if __name__ == "__main__":
    L = [1, 2, 3, 2, 4, 2, 5]
    repeat(L)