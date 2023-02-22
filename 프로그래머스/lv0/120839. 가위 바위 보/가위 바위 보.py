def solution(rsp):
    result = ""
    for i in range(len(rsp)):
        if rsp[i] == '2':
            result += '0'
        elif rsp[i] == '0':
            result += '5'
        else:
            result += '2'
    return result