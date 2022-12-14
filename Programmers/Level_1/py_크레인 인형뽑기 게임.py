# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64061#

def solution(board, moves):
    answer = []
    cnt = 0
    board = list(map(lambda y : list(filter(lambda f : f > 0, list(map(lambda x : x[y], board)))), range(len(board))))
    for i in moves :
        if len(board[i-1]) > 0 :
            answer.append(board[i-1][0])
            board[i-1].pop(0)
        if len(answer) >= 2 and answer[-1] == answer[-2] :
            cnt += 2
            answer = answer[:-2]
    return cnt