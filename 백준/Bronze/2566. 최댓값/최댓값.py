import sys
I = sys.stdin.readline

A = []
for _ in range(9):
    A.append(list(map(int,I().split())))

max_value = A[0][0]
max_row = 1
max_col = 1

for i in range(9):
    for j in range(9):
        if A[i][j] > max_value:
            max_value = A[i][j]
            max_row = i+1
            max_col = j+1
        else:
            pass

print(max_value)
print(max_row, max_col)