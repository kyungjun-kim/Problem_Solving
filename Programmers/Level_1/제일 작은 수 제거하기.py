def solution(arr):
    answer = arr.copy()
    arr.sort(reverse = True)
    answer.remove(arr[-1])
    if len(answer) == 0 :
        answer.append(-1)
    return answer