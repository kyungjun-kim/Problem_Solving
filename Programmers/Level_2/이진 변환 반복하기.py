# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0,0]
    while True :
        answer[0] += 1 
        answer[1] += s.count('0')
        s = str(bin(len(str(s).replace("0",''))))[2:]
        if str(s) == '1':
            break
    return answer