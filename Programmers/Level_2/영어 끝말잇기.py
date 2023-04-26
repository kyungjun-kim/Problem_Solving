# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    word = words[0][0]
    for i,j in enumerate(words) :
        if j[0] != word[-1] or words[i] in words[:i]:
            return [i%n+1,i//n+1]
        word = j
    return [0,0]