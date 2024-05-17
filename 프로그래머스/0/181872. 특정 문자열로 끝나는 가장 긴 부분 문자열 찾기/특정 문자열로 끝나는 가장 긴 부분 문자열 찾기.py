def solution(myString, pat):
    return myString[::-1][myString[::-1].index(pat[::-1]):][::-1]