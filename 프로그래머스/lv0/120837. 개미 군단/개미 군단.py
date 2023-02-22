def solution(hp):
    result = 0
    if hp% 5 != 0:
        result += hp//5 + hp%5//3
        if hp%5%3 != 0:
            result += hp%5%3
    else:
        result = hp//5
    return result