def check(arr):
    
    if arr == sorted(arr):
        print("sorted")
    else:
        print("not sorted")
        
        
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    check(arr)