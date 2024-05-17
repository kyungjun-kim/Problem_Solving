def solution(picture, k):
    answer = []
    for i in picture :
        for j in range(k) :
            tmp = ''
            for l in i :
                tmp += l*k
            answer.append(tmp)
    return answer