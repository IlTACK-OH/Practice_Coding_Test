def solution(n):
    pizza = 1
    while True:
        if (6*pizza)%n == 0:
            return pizza
        else:
            pizza += 1
            continue