for i in range(int(input())):
    num, in_str = input().split()
    num = int(num)
    print("".join([i*num for i in in_str]))