#5 , 3, 1
def solution(hp):
    answer = 0
    for i in [5, 3, 1] :
        answer += hp // i
        hp -= (hp // i) * i
    return answer