A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
number = [0]*10
for i in result:
    number[int(i)] += 1
for num in number:
    print(num)