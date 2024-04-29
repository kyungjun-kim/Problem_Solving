def solution(myString, pat):
    answer = 0
    for i,j in enumerate(myString) :
        if pat == myString[i:len(pat)+i] :
            answer += 1
    return answer