n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
check=[]
for i in range(1,n+1):
    check.append(i)
sorted(check)
flag = True
for i in range(n):
    if sorted(matrix[i]) != check:
        flag = False
        break
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
    if sorted(matrix[i]) != check:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")