def solution(my_string, num1, num2):
    answer =''
    for index, string in enumerate(my_string):
        if index == num1:
            answer += my_string[num2]
        elif index == num2:
            answer += my_string[num1]
        else:
            answer += string
    return answer
    