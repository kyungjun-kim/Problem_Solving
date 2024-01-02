def solution(left, right):
    answer = []
    for i in range(left,right+1) :
        num = 0
        for j in range(1,int(i/2)+1) :
            if i%j == 0 :
                num += 1
        if num%2 != 0:
            answer.append(i)
        else :
            answer.append(-i)
    return sum(answer)