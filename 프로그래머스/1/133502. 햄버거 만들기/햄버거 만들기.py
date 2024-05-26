def solution(ingredient):
    answer = 0
    result = []
    for i in ingredient :
        result.append(i)
        while len(result) > 3 and result[-4:] == [1,2,3,1]:
            answer += 1
            for p in range(4) :
                result.pop()
    return answer