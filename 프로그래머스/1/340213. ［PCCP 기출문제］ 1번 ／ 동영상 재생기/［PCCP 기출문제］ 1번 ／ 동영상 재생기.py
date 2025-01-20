def change(string) :
    tmp = list(map(lambda x : int(x), string.split(":")))
    return tmp[0]*60 + tmp[1]

def solution(video_len, pos, op_start, op_end, commands):
    commands.append("")
    answer = change(pos)
    
    for c in commands :
        if change(op_start) <= answer <= change(op_end) :
            answer = change(op_end)    
        if c == "next" :
            answer = min(answer+10, change(video_len))
        elif c == "prev" :
            answer = max(answer-10, 0) 
            
    M, S = answer // 60, answer % 60
    return "{}:{}".format(str(M) if M > 10 else f"0{M}" , str(S) if S > 10 else f"0{S}")