import sys

I = sys.stdin.readline

total_case = int(I())
result_list =[]

for _ in range(total_case):
    num_1, num_2 = map(int,I().split())
    result_list.append(num_1+num_2)

for i in range(total_case):
    print(f"Case #{i+1}: {result_list[i]}")