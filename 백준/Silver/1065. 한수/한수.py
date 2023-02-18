N = int(input())
if N < 100:
    print(N)

else:
    result = 99
    for i in range(110,N+1):
        str_num = str(i)
        if int(str_num[0])-2*int(str_num[1])+int(str_num[2])== 0:
            result += 1
    print(result)