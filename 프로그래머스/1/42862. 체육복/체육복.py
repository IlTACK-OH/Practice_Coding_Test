def solution(n, lost, reserve):
    reserve.sort()
    l_and_r = []
    for i in reserve:
        if i in lost:
            lost.remove(i)
            l_and_r.append(i)
    
    for j in l_and_r:
        reserve.remove(j)
    print(reserve)
    for k in reserve:
        can_bor = [k-1, k+1]
        for num in can_bor:
            if num  in lost:
                lost.remove(num)
                break
            
    return n - len(lost)