import sys

I = sys.stdin.readline

N = int(I())
in_list = list(map(int,I().split()))
v = int(I())

print(in_list.count(v))