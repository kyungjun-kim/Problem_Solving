def solution(participant, completion):
    p,c = participant, completion
    answer = ''
    """
    for i in participant :
        if i in completion :
            completion.remove(i)
        else :
            answer = i """
    import collections as co
    if len(p) != len(set(p)) : #중복이 있는 경우
        answer = list((co.Counter(p) - co.Counter(c)).keys())[0]
    else : # 중복이 없는 경우
        answer = list(set(p) - (set(c)))[0]
    return answer