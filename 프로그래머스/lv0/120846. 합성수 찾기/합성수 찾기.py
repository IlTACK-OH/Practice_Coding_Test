def solution(n):
    if n <= 3:
        return 0
    count = 3
    for i in range(4, n+1):
        sosu=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0: 
                sosu = False
                break
        if sosu:
            count += 1
    return n-count