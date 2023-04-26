#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    result = [0,0]
    for i in lottos :
        if i in win_nums :
            result[0] += 1
            result[1] += 1
        elif i == 0 :
            result[0] += 1
    answer = list(map(lambda x : 7-x if x > 1 else 6, result))
    return answer