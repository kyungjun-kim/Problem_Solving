#문제풀이 : https://school.programmers.co.kr/learn/courses/30/lessons/160586#
def solution(keymap, targets):
    answer = list(map(lambda x : 0, targets))
    for t_num, target in enumerate(targets) :
        for t in target :
            km = list(filter(lambda f : t in f, keymap))
            if km == [] :
                answer[t_num] = -1
                break
            else :
                answer[t_num] += min(list(map(lambda x : x.index(t), km)))+1
                #print(km,list(map(lambda x : x.index(t), km)))
    return answer