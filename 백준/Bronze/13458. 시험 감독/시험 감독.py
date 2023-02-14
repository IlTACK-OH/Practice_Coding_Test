N = int(input())
A_i = list(map(int,input().split()))
B, C = map(int,input().split())

result = []

for i in A_i:
    if B >= i:
        result.append(0)
    elif (i-B)%C == 0:
        x = int((i-B)/C)
        result.append(x)
    else:
        x = int((i-B)/C) + 1
        result.append(x)

print(sum(result)+N)