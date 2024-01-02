import numpy as np
num_array = np.array([[1,2,3],[4,5,6],[7,8,9],['*',0,"#"]])
def solution(numbers, hand):
    answer = ''
    rthumb = np.where(num_array == '*')
    lthumb = np.where(num_array == '#')
    for i in numbers :
        if np.where(num_array == str(i))[1] == 0 :
            answer += 'L'
            lthumb = np.where(num_array == str(i))
        elif np.where(num_array == str(i))[1] == 2 :
            answer += 'R'
            rthumb = np.where(num_array == str(i))
        else :
            if abs(rthumb[0]-np.where(num_array == str(i))[0]) + abs(rthumb[1]-np.where(num_array == str(i))[1]) < abs(lthumb[0]-np.where(num_array == str(i))[0]) + abs(lthumb[1]-np.where(num_array == str(i))[1]) :
                answer += 'R'
                rthumb = np.where(num_array == str(i))
            elif abs(rthumb[0]-np.where(num_array == str(i))[0]) + abs(rthumb[1]-np.where(num_array == str(i))[1]) > abs(lthumb[0]-np.where(num_array == str(i))[0]) + abs(lthumb[1]-np.where(num_array == str(i))[1]) :
                answer += 'L'
                lthumb = np.where(num_array == str(i))
            else :
                answer += hand.upper()[0]
                if hand == 'right' :
                    rthumb = np.where(num_array == str(i))
                else :
                    lthumb = np.where(num_array == str(i))
    return answer