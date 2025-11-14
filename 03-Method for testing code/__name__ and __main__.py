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
        
'''
Every python file has a spacial built-in variable called __name__.
If the file is being run directly then python sets __name__ = __main__.
If the file is imported as a module int anther file the python sets __name__ = "--modulename--"


This prevents accidental code execution when importing.
lets the file be both a script and a module at the same time .

This says: Only run this code when the file is executed directly

'''