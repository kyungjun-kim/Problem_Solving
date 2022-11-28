def solution(s):
    numstr, answer = '',''
    num_list = ['zero','one','two','three','four','five','six','seven','eight','nine'] #리스트 지정
    for i in range(len(s)) : 
        if s[i].isdigit() : #숫자일 경우 그대로 입력
            if numstr == '' :
                answer += s[i]
            else :
                answer += str(num_list.index(numstr)) + s[i]
                numstr = ''
        else : #알파벳일 경우 문자열을 합친 후 num_list와 비교해 숫자로 변환
            numstr += s[i]
            if numstr in num_list :
                answer += str(num_list.index(numstr))
                numstr = ''            
    return int(answer)