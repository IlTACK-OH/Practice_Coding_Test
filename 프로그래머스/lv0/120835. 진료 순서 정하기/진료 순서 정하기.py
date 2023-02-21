def solution(emergency):
    sort_emer = sorted(emergency,reverse=True)
    result = []
    for i in emergency:
        result.append(sort_emer.index(i)+1)
    return result