# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/132267#

def solution(a, b, n):
    cnt, answer = 0,0
    #print(n,a,'\n')
    while n >= a :
        tmp = n // a * b
        num = n % a
        answer += tmp
        n = tmp + num
        #print('og : {}, 받은 병 : {} , 누적 병 {}'.format(n,tmp,answer))
        cnt += 1
    return answer