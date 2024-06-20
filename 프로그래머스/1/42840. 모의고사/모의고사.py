def solution(answers):
    ans_len = len(answers)//40 + 1
    ans_1 = [1, 2, 3, 4, 5]*8*ans_len
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]*5*ans_len
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*4*ans_len
    score = [0,0,0]
    
    for idx, ans in enumerate(answers):
        if ans == ans_1[idx]:
            score[0] += 1
        if ans == ans_2[idx]:
            score[1] += 1
        if ans == ans_3[idx]:
            score[2] += 1
    score = [(score[0],1), (score[1],2), (score[2],3)]
    score.sort(reverse = True)
    answer = [score[0][1]]
    max_score = score[0][0]
    for sco, num in score[1:]:
        if sco == max_score:
            answer.append(num)
    answer.sort()
    return answer