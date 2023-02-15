import sys

I = sys.stdin.readline
input_list= []

for _ in range(3):
    input_list.append(list(map(int,I().split())))

if input_list[0][0] == input_list[1][0]:
    x = input_list[2][0]
elif input_list[1][0] == input_list[2][0]:
    x = input_list[0][0]
elif input_list[0][0] == input_list[2][0]:
    x = input_list[1][0]
    
if input_list[0][1] == input_list[1][1]:
    y = input_list[2][1]
elif input_list[0][1] == input_list[2][1]:
    y = input_list[1][1]
elif input_list[1][1] == input_list[2][1]:
    y = input_list[0][1]
    
print(x,y)