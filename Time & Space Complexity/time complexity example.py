#Here we will use the most common time complexity mathmatical function big-O notation

# O(1)
num1 = 10
num2 = 20
result1 = num1+num2

# O(1)
n = int(input())
result2 = n * (n+1)/2

# O(n) this time complexity is very bad in compare of O(1)
n = int(input())
result3 = 0
for i in range(1, n+1):
    result3 += i