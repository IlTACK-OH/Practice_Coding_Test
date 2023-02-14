import sys
I = sys.stdin.readline

N = int(I())

input_list=[]

for _ in range(N):
    input_list.append(int(I()))

input_list.sort()

for i in input_list:
    print(i)