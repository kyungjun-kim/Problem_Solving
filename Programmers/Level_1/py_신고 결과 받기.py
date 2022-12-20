# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    result = list(map(lambda x : [x.split()[0],x.split()[1]] , set(report)))
    b = list(map(lambda x : x.split()[1] , set(report)))
    kk = list(map(lambda x : x if b.count(x) >= k else '_' ,id_list))
    for i in result :
        if i[1] in kk :
            #print(i)
            answer.append(i[0])
    answer = list(map(lambda x : answer.count(x), id_list))
    #print(result,'\n\n',b,'\n\n',kk, '\n\n', answer)
    return answer