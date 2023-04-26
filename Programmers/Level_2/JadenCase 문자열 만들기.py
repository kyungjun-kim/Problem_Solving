# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = []
    for i in s.lower().split(" ") :
        if i.isalpha() :
            answer.append(i[0].upper() + i[1:])
        else :
            answer.append(i)
    return " ".join(answer)