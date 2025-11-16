def average(L):
    if not L:
        return None
    
    return sum(L)/len(L)

if __name__ == "__main__":
    L = [1,2,3,4,5,6]
    expected = 3.0
    result = average(L)
    print(f"Expected: {expected}, Got: {result}")
    assert expected == result, "average() produced incorrect result"
    print("All tests passed!")