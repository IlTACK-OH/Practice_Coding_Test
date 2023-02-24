def solution(n):
    num = 1
    while True:
        result = 1
        for i in range(1, num+1):
            result = result*i
        if result == n:
            return num
        elif result > n:
            return num - 1
        num += 1