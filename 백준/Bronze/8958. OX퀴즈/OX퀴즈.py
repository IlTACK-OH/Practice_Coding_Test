N = int(input())
for _ in range(N):
    ox_case = input()
    score = 0
    o_num = 0
    for i in ox_case:
        if i =="X":
            o_num = 0
        else:
            o_num += 1
            score += o_num
    print(score)
        