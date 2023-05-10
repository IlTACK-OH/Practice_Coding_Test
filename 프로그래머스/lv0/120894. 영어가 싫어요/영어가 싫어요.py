def solution(numbers):
    num_str = ["zero",'one','two','three','four','five','six','seven',
                   'eight','nine']
    for i in range(len(num_str)):
        numbers = numbers.replace(num_str[i],f'{i}')
    return int(numbers)