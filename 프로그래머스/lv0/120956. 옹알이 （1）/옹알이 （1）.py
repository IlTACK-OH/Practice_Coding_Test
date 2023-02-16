import re
def solution(babbling):
    result = 0
    for i in babbling:
        answer = re.sub('aya|ye|woo|ma', "",i)
        if answer == "":
            result += 1
    return result