def avarage(L):
    if not L:
        return None
    return sum(L)/len(L)

if __name__ == "__main__":
    L = [1,2,3,4,5]
    expected = 3.0
    result = avarage(L)
    
    if expected == result:
        print("test passed")
    else:
        print("test failed!", "received:",result, "expected:",expected)