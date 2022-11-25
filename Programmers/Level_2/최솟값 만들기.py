# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A.sort(reverse = False), B.sort(reverse = True)
    for i in range(len(A)) :
            answer += A[i]*B[i]
    return answer