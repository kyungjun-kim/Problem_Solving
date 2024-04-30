def solution(myString):
    return ''.join(list(map(lambda x : x if x > "l" else "l", myString)))