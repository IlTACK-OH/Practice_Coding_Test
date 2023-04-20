def solution(a, b):
    result1 = int(f"{a}{b}")
    result2 = 2*a*b
    if result1 >= result2:
        return result1
    else:
        return result2
