def solution(s, n):
    answer = list(s)
    for i in range(len(answer)) :
        if answer[i].isalpha() == True :
            if 65 <= ord(answer[i]) <= 90 :
                if ord(answer[i]) + n > 90 :
                    answer[i] = chr(ord(answer[i]) + n - 26)
                else :
                    answer[i] = chr(ord(answer[i]) + n)
            elif 97 <= ord(answer[i]) <= 122 :
                if ord(answer[i]) + n > 122 :
                    answer[i] = chr(ord(answer[i]) + n - 26) 
                else :
                    answer[i] = chr(ord(answer[i]) + n)
    return "".join(answer)