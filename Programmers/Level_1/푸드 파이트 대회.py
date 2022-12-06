# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    f = list(map(lambda x : x-1 if x % 2 == 1 else x, food[1:]))
    answer = ''
    for i in range(len(f)) :
        for j in range(f[i]//2) :
            answer += str(i+1)
    answer = answer + '0' + answer[::-1]
    return answer