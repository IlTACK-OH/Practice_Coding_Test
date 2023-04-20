def solution(my_string):
    num_list = [int(i) for i in my_string if i.isdigit()]
    answer = 0
    for i in num_list:
        answer += i
    return answer