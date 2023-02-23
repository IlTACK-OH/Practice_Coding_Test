def solution(dot):
    one = (dot[0] > 0) and (dot[1] > 0)
    two = 2*((dot[0] < 0) and (dot[1] > 0))
    three = 3*((dot[0] < 0) and (dot[1] < 0))
    four = 4*((dot[0] > 0) and (dot[1] < 0))
    return one + two + three + four
