def solution(rank, attendance):
    answer = sorted(list(filter(lambda x : x[1] == True, zip(rank, attendance,range(len(rank))))), key=lambda x : x[0])[:3]
    return 10000 * answer[0][2] + 100 * answer[1][2] + answer[2][2]