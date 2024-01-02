#문제풀이 : https://school.programmers.co.kr/learn/courses/30/lessons/172928#
def solution(park, routes):
    for i in range(len(park)) :
        if "S" in park[i] :
            now = [i,park[i].index("S")]
            break
    park = list(map(lambda x : list(tuple(x)), park))    
    #print("first now = {}".format(now))
    for i in routes :
        try :
            num = int(i.split()[1])
            if i[0] == "S" :
                if now[0] + num >= len(park) or "X" in list(map(lambda x : x[now[1]] , park))[now[0]+1:now[0]+num+1]:
                    continue
                else :
                    park[now[0]][now[1]] = '0'
                    now[0] += num
                    park[now[0]][now[1]] = 'S'
            elif i[0] == "N" :
                if now[0] - num < 0  or "X" in list(map(lambda x : x[now[1]] , park))[now[0]-num:now[0]]:
                    continue
                else :
                    park[now[0]][now[1]] = '0'
                    now[0] -= num
                    park[now[0]][now[1]] = 'S'
            elif i[0] == "E" :
                if now[1] + num >= len(park[0]) or "X" in park[now[0]][now[1]+1:now[1]+1+num]:
                    continue
                else :
                    park[now[0]][now[1]] = '0'
                    now[1] += num
                    park[now[0]][now[1]] = 'S'
            elif i[0] == "W" :
                if now[1] - num < 0 or "X" in park[now[0]][now[1]-num:now[1]]:
                    continue
                else :
                    park[now[0]][now[1]] = '0'
                    now[1] -= num
                    park[now[0]][now[1]] = 'S'
        except Exception as e :
            print(e)
    return now