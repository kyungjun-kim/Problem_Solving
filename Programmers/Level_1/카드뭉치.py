# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/159994
def solution(cards1, cards2, goal):
    try :
        for i in range(len(cards1) + len(cards2)) :
            if len(cards1) > 0 and cards1[0] == goal[0] :
                cards1 = cards1[1:]
                goal = goal[1:]
            elif len(cards2) > 0 and cards2[0] == goal[0] :
                cards2 = cards2[1:]
                goal = goal[1:]                
            else :
                return "No"
            if len(goal) == 0 :
                return "Yes"
    except :
        return "No"
