# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    name = {}
    answer = []
    for i in record :
        if i.startswith("Enter"):
            name[i.split()[1]] = i.split()[2]
            answer.append("{}님이 들어왔습니다.".format(i.split()[1]))
        elif i.startswith("Leave"):
            answer.append("{}님이 나갔습니다.".format(i.split()[1]))
        else :
            name[i.split()[1]] = i.split()[2]
    answer = list(map(lambda x : "{}님이 {}".format(name[x.split()[0][:-2]], x.split()[1]) , answer))
    return answer