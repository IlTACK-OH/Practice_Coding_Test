def solution(numbers, direction):
    if direction == "right":
        last = numbers[-1]
        numbers[1:] = numbers[0:-1]
        numbers[0] = last
        return numbers
    else:
        first = numbers[0]
        numbers[0:-1] = numbers[1:]
        numbers[-1] = first
        return numbers
    