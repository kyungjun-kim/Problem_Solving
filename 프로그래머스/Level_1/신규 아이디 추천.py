def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for i in new_id :
        if answer == '' and i == '.' :
            continue
        if i.isalnum() or i in ['-','_','.'] :
            if len(answer) >= 1 and answer[-1] == '.' and i == '.' :
                continue
            else :
                answer += i
    if len(answer) != 0 and answer[-1] == '.' :
        answer = answer[:-1]
    elif len(answer) == 0 :
        answer = 'a'
        
    if len(answer) > 15 :
        while len(answer) > 15 or answer[-1] == '.' :
            answer = answer[:-1]
    if len(answer) < 3 :
        while len(answer) < 3 :
            answer += answer[-1]   
    return answer