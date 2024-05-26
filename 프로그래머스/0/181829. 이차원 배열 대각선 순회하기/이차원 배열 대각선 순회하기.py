def solution(board, k):
    answer = 0
    for i , j in enumerate(board) :
        for m, l in enumerate(j) :
            if i + m <= k :
                answer += l
    return answer