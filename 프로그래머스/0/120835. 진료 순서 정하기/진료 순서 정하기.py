def solution(emergency):
    tmp = sorted(emergency, reverse = True)
    result = []
    for i in emergency :
        result.append(tmp.index(i)+1)
    return result