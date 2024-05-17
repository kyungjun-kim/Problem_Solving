def solution(bandage, health, attacks):
    check_time = 0
    h = health
    for i in attacks :
        time_diff = i[0]-check_time
        check_time = i[0]+1
        h += time_diff * bandage[1]
        h += (time_diff//bandage[0]) * bandage[2]
        h = min(health,h)
        h -= i[1]
        if h <= 0 :
            return -1
        #print("attack :{}, 체력 : {}, 시간차 : {}, 시간계산 : {}".format(i,h,time_diff,time_diff//bandage[0]))
    return h