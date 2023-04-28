def solution(s):
    s_list = s.split(" ")
    answer = 0

    for i in s_list:
        if i != "Z":
            num = int(i)
            answer += num
            before = num
            
        if i == "Z":
            answer -= before
    return answer