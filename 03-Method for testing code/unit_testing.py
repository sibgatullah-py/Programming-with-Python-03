# there are some built in unit testing packages availabel such as unittest
# but there is another third party package called pytest . this one is populer cause it's easy to use

def average(L):
    if not L:
        return None
    
    return sum(L)/len(L)

def test_average():
    assert 3.0 == average([1,2,3,4,5])