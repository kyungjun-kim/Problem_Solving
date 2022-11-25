# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    answer = []
    for i in operations :
        if i[0] == 'I' :
            answer.append(int(i[2:]))
        elif i[0] == 'D' and len(answer) > 0  : 
            if i[2].isdigit() :
                answer.remove(max(answer))
            else :
                answer.remove(min(answer))
    if len(answer) > 1 :
        return [max(answer),min(answer)]
    else :
        return [0,0]