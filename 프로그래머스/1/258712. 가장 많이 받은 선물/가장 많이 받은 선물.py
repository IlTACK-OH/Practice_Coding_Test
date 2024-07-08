def solution(friends, gifts):
    history = {} # 초기화
    # 딕셔너리 생성
    for name in friends:
        history[name] = {}
        for other in friends:
            if other == name:
                continue
            history[name][other] = 0
    
    # 선물 주고받기 정리       
    for give_receive in gifts:
        giver, receiver = give_receive.split()
        history[giver][receiver] += 1
        history[receiver][giver] -= 1
    
    # 선물지수 계산
    gift_score = {}
    for name in friends:
        gift_score[name] = sum(history[name].values())
    
    max_gift = 0 # 다음달에 받을 선물 최대 갯수 초기화
    
    # 받을 선물 계산
    for name, hist_dict in history.items():
        name_score = gift_score[name]
        next_gift = 0
        for other, hist in hist_dict.items():
            if hist > 0:
                next_gift += 1
            elif hist == 0:
                if name_score>gift_score[other]:
                    next_gift += 1
                    
        if next_gift > max_gift:
            max_gift = next_gift
    
    return max_gift