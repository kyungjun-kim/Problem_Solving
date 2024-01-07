def solution(board, h, w):
    c_list = [board[h][min(w+1,len(board[0])-1)], 
             board[h][max(w-1,0)],
             board[min(h+1,len(board[0])-1)][w],
             board[max(h-1,0)][w]]
    if h == len(board)-1 :
        c_list[2] = ''
    if h == 0 :
        c_list[3] = ''
    if w == len(board)-1 :
        c_list[0] = ''
    if w == 0 :
        c_list[1] = ''
    return len(list(filter(lambda x : x == board[h][w], c_list)))