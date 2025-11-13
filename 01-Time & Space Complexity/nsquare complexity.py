# when there is nested loops of any kind it becomes O(n*n)

n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        count += 1
        
print(count)

# if 3 loops gets on each other like these nested lops then it becomes cube O(n*n*n)