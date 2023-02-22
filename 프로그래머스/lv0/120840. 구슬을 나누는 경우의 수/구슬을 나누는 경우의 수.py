def solution(balls, share):
    num_n = 1
    num_m = 1
    num_n_m = 1
    bal_share = balls-share
    for i in range(2,balls+1):
        num_n = num_n*i
    for i in range(2,share+1):
        num_m = num_m*i
    for i in range(2, bal_share+1):
        num_n_m = num_n_m*i
    return num_n/(num_m*num_n_m)