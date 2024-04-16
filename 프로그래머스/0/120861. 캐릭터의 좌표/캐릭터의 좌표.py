def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput :
        tmp = answer.copy()
        if i == "left" :
            answer[0] -= 1
        elif i == "right" :
            answer[0] += 1
        elif i == "up" :
            answer[1] += 1
        elif i == "down" :
            answer[1] -= 1
        if abs(answer[1]) > board[1]//2 or abs(answer[0]) > board[0]//2 :
            answer = tmp.copy()
    return answer