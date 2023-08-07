#문제 풀이 : https://school.programmers.co.kr/learn/courses/30/lessons/140108
def solution(s):
    answer = 0
    while len(s) > 0 :
        x,a,b,tmp = s[0],0,0,'N'
        for i,j in enumerate(s[:]) :
            if j == x :
                a += 1
            else :
                b += 1
            if a == b :
                s = s[i+1:]
                tmp = 'Y'
                answer += 1
                break
        if tmp == 'N' :
            return answer + 1
    return answer