def solution(picks, minerals):
    answer = 0
    result = []
    for i in range(0,len(minerals),5) :
        pl = minerals[i:i+5]
        result.append([pl.count("diamond"),pl.count("iron"),pl.count("stone")])
    result = result[:sum(picks)]
    result = sorted(result,key=lambda x : [-((x[0] * 25) + (x[1] * 5) + x[2]), sum(x), -x[0]])    
    
    for i in result :
        if picks[0] > 0 :
            #print("다이아 곡괭이")
            answer += i[0] + i[1] + i[2]
            picks[0] -= 1
        elif picks[1] > 0 :
            #print("철 곡괭이")
            answer += (i[0] * 5) + i[1] + i[2]
            picks[1] -= 1
        elif picks[2] > 0 :
            #print("돌 곡괭이")
            answer += (i[0] * 25) + (i[1] * 5) + i[2]
            picks[2] -= 1
        if sum(picks) == 0 :
            return answer
    return answer
