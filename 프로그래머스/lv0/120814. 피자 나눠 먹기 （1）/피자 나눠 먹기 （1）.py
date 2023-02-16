def solution(n):
    pizza = 1
    
    while True:
        if 7*pizza//n >= 1:
            return pizza
        else:
            pizza += 1