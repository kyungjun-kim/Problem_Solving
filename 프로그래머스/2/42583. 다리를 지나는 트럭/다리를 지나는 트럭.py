from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque(0 for x in range(bridge_length))
    truck_weights = deque(truck_weights)
    tsum = 0 
    
    while len(truck_weights) > 0 :
        tsum -= que.popleft()
        if tsum + truck_weights[0] <= weight:
            t = truck_weights.popleft()
            tsum += t
            que.append(t)
        else :
            que.append(0)
        answer += 1
    return answer + bridge_length